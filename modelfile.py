from google.appengine.ext import ndb
class UserProfile(ndb.Model):
    """Model for User Profiles"""
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    user_id = ndb.StringProperty()

class Message(ndb.Model):
    text = ndb.StringProperty()
    sender = ndb.StringProperty()
    receiver = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)