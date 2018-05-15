
import logging

from flask import render_template, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import required
from myapp.models.phrase import Phrase

import urllib
import urllib2
import json

from myapp import app


MASHAPE_KEY = 'your-mashape-key'


class MyForm(FlaskForm):
    text = StringField('text', [required()])
    submit = SubmitField('Submit', [required()])


@app.route('/analyzer', methods=['GET'])
def showForm():
    form = MyForm()
    return render_template('sentiment.html', form=form)


@app.route('/analyzer', methods=['POST'])
def submitForm():
    form = MyForm(request.form)
    if not form.validate():
        return render_template('/analyzer', form=form), 400

    text_inserted = form.text.data

    # use Mashape API
    url = 'https://text-sentiment.p.mashape.com/analyze'

    params = urllib.urlencode({'text': text_inserted})

    req = urllib2.Request(url, params)
    req.add_header('X-Mashape-Key', MASHAPE_KEY)
    req.add_header('Accept', 'application/json')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    urlopen = urllib2.urlopen(req)
    content = urlopen.read()
    risp = json.loads(content)

    pos = risp['pos']
    neg = risp['neg']
    logging.info('The text inserted is {} pos and {} neg'.format(pos, neg))

    if pos == 1 and neg == 0:
        flash('The sentence inserted is 100% positive!')
    elif pos == 0 and neg == 1:
        flash('The sentence inserted is 100% negative!')
    else:
        flash('The sentence inserted is 50% positive and 50% negative!')

    # save result in the Datastore
    qry = Phrase.query(Phrase.text==text_inserted).get()

    if not qry:
        if pos == 1 and neg == 0:
            new_p = Phrase(text=text_inserted, pos=True, counter=1)
            new_p.put()
        elif pos == 0 and neg == 1:
            new_p = Phrase(text=text_inserted, neg=True, counter=1)
            new_p.put()
        else:
            new_p = Phrase(text=text_inserted, pos=True, neg=True, counter=1)
            new_p.put()
        logging.info('Correctly inserted the text in the Datastore')
    else:
        qry.counter = qry.counter+1
        qry.put()
        logging.info('Correctly updated the text in the Datastore')

    return redirect('/')
