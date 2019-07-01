from modelfile import *
import json

def post_info():
    data = UserProfile.query().fetch()
    row = []
    for x in data:
        row.append({
            'first_name': x.first_name,
            'last_name' : x.last_name,
            'key' : x.key.urlsafe(),
            'email' : x.email
        })
    self.response.write(json.dumps(row))

def post_data(user_email):
    user = UserProfile()
    user.email = user_email
    user.put()
