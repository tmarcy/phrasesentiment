from flask import render_template

from myapp import app


@app.route('/')
def homepage():
    handlers = [
        ('analyzer', ('/analyzer')),
        ('statistics', '/api/1/sentiment/getstats')
    ]
    return render_template('home.html', handlers=handlers)
