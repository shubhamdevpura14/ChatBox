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

class MsHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        messageq = json.loads(self.request.body)
        sender = user.email()
        receiver = messageq.get('receiver')
        chats = Message.query(Message.sender.IN([sender,receiver]) , Message.receiver.IN([sender,receiver])).\
                               order(-Message.date).fetch()
        d=[]
        for x in chats:
            d.append({
                'text': x.text,
                'receiver': x.receiver,
                'sender': x.sender
            })  
        self.response.write(json.dumps(d))

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
    ('/handlers/Contacts', Contacts),
    # ('/handlers/Userinfo', Userinfo),
])
