from flask import Flask
from flask_wtf.csrf import CSRFProtect

import logging
import appengine_config
import myapp.app_config

app = Flask(__name__)
app.config.from_object(__name__)

if appengine_config.GAE_DEV:
    logging.warning('using a dummy secret key')
    app.secret_key = 'my-secrete-key'
    app.debug = True
else:
    app.secret_key = myapp.app_config.app_secret_key

DEBUG = True
csrf_protect = CSRFProtect(app)
