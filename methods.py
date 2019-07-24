from google.appengine.api import users
from modelfile import *
import json
import time

def post_info():
    data = UserProfile.query().fetch()
    row = []
    for x in data:
        row.append({
            'key' : x.key.urlsafe(),
            'email' : x.email
         })
    self.response.write(json.dumps(row))

def post_data(user_email):
    user = UserProfile()
    user.email = user_email
    user.put()

def put_user():
    user = users.get_current_user()
    user_email = user.email()
    check_user = UserProfile.query(UserProfile.email == user_email).get()
    if not check_user:
        post_data(user_email)
    return user_email   