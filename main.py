import webapp2
from modelfile import *
import json
from google.appengine.api import users
from methods import *

class Messageinfo(webapp2.RequestHandler):
    def post(self):
        put_user()
        time.sleep(1)
        messageq = json.loads(self.request.body)
        print messageq
        user = users.get_current_user()
        message = Message()
        message.sender = user.email()
        message.text = messageq.get('text')
        message.receiver = messageq.get('receiver')
        message.put()
        self.response.out.write("Done")

# class Userinfo(webapp2.RequestHandler):
#     def post(self):
        
#         user1 = json.loads(self.request.body)selected
#         print user1
#         userr = UserProfile()
#         userr.user = user1.get('username')
#         userr.put()
#         self.response.out.write("Done")

class MsHandler(webapp2.RequestHandler):
    def get(self):
        put_user()
        time.sleep(1)
        qry = Message.query().order(Message.date)
        d=[]
        for x in qry:
            d.append({
                'text': x.text,
                'receiver': x.receiver,
                'sender': x.sender
            })   
        self.response.out.write(json.dumps(d))


class Contacts(webapp2.RequestHandler):
    def get(self):
        owner_email = put_user()
        time.sleep(1)
        user = users.get_current_user()
        user_email = user.email()
        data =  UserProfile.query(UserProfile.email != user_email).fetch()
        d=[]
        for x in data:
            d.append({
                'email': x.email,
                'key': x.key.urlsafe()
            })
        
        print(user_email)
        self.response.write(json.dumps({"d" : json.dumps(d), "current_user" : owner_email}))
                

class Mainpage(webapp2.RequestHandler):
    def get(self):
        # def get(self):
        
        self.redirect("/chat#!/chat")
        
        
             

app = webapp2.WSGIApplication([
    webapp2.Route('/', Mainpage),
    ('/handlers/get', MsHandler),
    ('/handlers/save',Messageinfo),
    # ('/handlers/submit', Submit),
    ('/handlers/Contacts', Contacts),
    # ('/handlers/Userinfo', Userinfo),
])
