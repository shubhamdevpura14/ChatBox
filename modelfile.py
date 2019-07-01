from google.appengine.ext import ndb
class UserProfile(ndb.Model):
    """Model for User Profiles"""
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    user_id = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.TextProperty()
    sender = ndb.StringProperty()
    receiver = ndb.StringProperty()


class User(ndb.Model):
    text = ndb.StringProperty()
    user = ndb.StringProperty()
    password = ndb.StringProperty()
    username = ndb.StringProperty()