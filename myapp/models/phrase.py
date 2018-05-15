
from google.appengine.ext import ndb


class Phrase(ndb.Model):
    """ Phrase structured model in the Datastore.
        Pos is set to True if the phrase sentiment is positive.
        Neg is set to True if the phrase sentiment is negative.
        Counter counts how many times the text is requested.
        Date saves the date-time of the request.
    """
    text = ndb.StringProperty()
    pos = ndb.BooleanProperty(default=False)
    neg = ndb.BooleanProperty(default=False)
    counter = ndb.IntegerProperty(default=0)
    date = ndb.DateTimeProperty(auto_now_add=True)

