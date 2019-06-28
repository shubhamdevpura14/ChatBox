from google.appengine.ext import ndb
class Message(ndb.Model):
    user = ndb.StringProperty()
    whom = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()

class User(ndb.Model):
    user = ndb.StringProperty()
    password = ndb.StringProperty()
