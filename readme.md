# Project Title

Phrase Sentiment Analyzer

## The project in short

Simple Google App Engine Web Application example with minimal style, written in Python 2.7, using Mashape site API 
(see references in "Built With" section).
The app is able to test the positive or negative sentiment of a sentence.

## Specifications

* A form is used to retrieve the sentences, inserted by user.
* The app response shows the Sentiment Analysis result as a flash message.
* The sentences (and the relative datetime) are saved automatically in the Datastore.
* An API GET is given; it shows statistics about positive or negative sentiment related to a specific interval of time,
in JSON format.

## Before starting
* Add a lib folder to the project, in which you have to install the libraries listed in "requirements.txt" file.
* You must be logged in Mashape Market site in order to use its API; the site, also, provide you with an API key: 
paste it in the variable named "MASHAPE_KEY", before you run this project.

## Built With

* [Google App Engine](https://cloud.google.com/appengine) - Platform used
* [Flask](http://flask.pocoo.org/) - The microframework for Python used
* [Text Sentiment Analysis Method](https://market.mashape.com/fyhao/text-sentiment-analysis-method) - API used

## Author

* **Marcella Tincani** - [Marcella](https://github.com/tmarcy)
