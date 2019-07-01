import webapp2
from modelfile import *
import json
from google.appengine.api import users
from methods import *

class MsgHandler(webapp2.RequestHandler):
    def post(self):
        
        messageq = json.loads(self.request.body)
        print messageq
        message = UserProfile()
        message.user = messageq.get('user')
        message.whom = messageq.get('whom')
        message.text = messageq.get('text')
        message.mail = messageq.get('mail')
        message.put()
        self.response.out.write("Done")

class MsHandler(webapp2.RequestHandler):
    def get(self):
        
        qry = UserProfile.query().order(UserProfile.date)
        d=[]
        for x in qry:
            d.append({
                'text': x.text,
                'key': x.key.urlsafe()
            })   
        self.response.out.write(json.dumps(d))

class Submit(webapp2.RequestHandler):
    def post(self):
        data =  json.loads(self.request.body)
        user = User()
        user.mail = data.get('mail')
        ref = user.put()

        users =  User.query().fetch()
        d=[]
        for x in users:
            d.append({
                'mail': x.mail,
                'key': x.key.urlsafe()
            })
        self.response.out.write(json.dumps(d))


class ListMsgs(webapp2.RequestHandler):
    def get(self):
        data =  UserProfile.query().fetch()
        d=[]
        for x in data:
            d.append({
                'email': x.email,
                'key': x.key.urlsafe(),
                'text': x.text
            })
        self.response.write(json.dumps(d))            

class Mainpage(webapp2.RequestHandler):
    def get(self):
        # def get(self):
        user = users.get_current_user()
        user_email = user.email()
        user_id = user.user_id()
        print(user_email)
        print(user_id)
        check_user = UserProfile.query(UserProfile.email == user_email).get()
        if not check_user:
            post_data(user_email)
        self.redirect("/chat#!/chat")
        
             

app = webapp2.WSGIApplication([
    webapp2.Route('/', Mainpage),
    # ('/handlers/submit', Submit),
    ('/handlers/get', MsHandler),
    ('/handlers/save',MsgHandler),
    ('/handlers/submit', Submit),
    ('/handlers/ListMsgs', ListMsgs),
])