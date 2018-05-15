
from myapp import app
from myapp.models.phrase import Phrase
from datetime import datetime

from flask import make_response, request
import json
import logging
from google.appengine.ext import ndb


# function for error messages
def raise_error(message='An error occured during a request', errorcode=500):

    json_response = {}

    # status of the json_response
    json_response['status'] = 'failure'
    json_response['message'] = message
    json_response['data'] = []
    response = make_response(json.dumps(json_response, ensure_ascii=True), errorcode)
    response.headers['content-type'] = 'application/json'
    return response


@app.route('/api/1/sentiment/getstats', methods=['GET'])
def showStat():
    # retrieve parameters from query string
    params = request.args

    required_param = ['month', 'year']
    for r in required_param:
        if r not in params:
            return raise_error(message='Parameter {} is missing'.format(r))

    month = int(request.args['month'])
    year = int(request.args['year'])

    # set the start_date and the end_date to retrieve data
    start_date = datetime.strptime('01/{:02d}/{:04d}'.format(month, year), '%d/%m/%Y')

    if month == 12:
        end_date = datetime.strptime('01/{:02d}/{:04d}'.format((month+1) % 12, year+1), '%d/%m/%Y')
    else:
        end_date = datetime.strptime('01/{:02d}/{:04d}'.format((month+1), year), '%d/%m/%Y')

    logging.info('start: {}, end; {}'.format(start_date, end_date))

    # retrieve data from the Datastore and build the response in json format
    qry = Phrase.query(
        ndb.AND(Phrase.date >= start_date,
                Phrase.date < end_date
                )).fetch()

    tot_pos = 0
    tot_neg = 0
    tot_posneg = 0

    for each in qry:
        if each.pos is False and each.neg is True:
            tot_neg = tot_neg + (1*each.counter)
        elif each.pos is True and each.neg is False:
            tot_pos = tot_pos + (1*each.counter)
        elif each.pos is True and each.neg is True:
            tot_posneg = tot_posneg + (1*each.counter)


    json_response = {}
    my_data = [{'tot_negative': tot_neg, 'tot_positive': tot_pos, 'negative&positive': tot_posneg}]

    # status of the json_response
    json_response['status'] = 'OK'
    json_response['message'] = 'Succesfully returned the resource.'
    json_response['data'] = my_data
    response = make_response(json.dumps(json_response, ensure_ascii=True), 200)
    response.headers['content-type'] = 'application/json'
    return response


