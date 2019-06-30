import webapp2
from modelfile import *
import json


class MsgHandler(webapp2.RequestHandler):
    def post(self):
        
        messageq = json.loads(self.request.body)
        print messageq
        message = Message()
        message.user = messageq.get('user')
        message.whom = messageq.get('whom')
        message.text = messageq.get('text')
        message.put()
        self.response.out.write("Done")

class MsHandler(webapp2.RequestHandler):
    def get(self):
        
        qry = Message.query().order(-Message.user)
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
        user.text = data.get('text')
        ref = user.put()

        users =  User.query().fetch()
        d=[]
        for x in users:
            d.append({
                'text': x.text,
                'key': x.key.urlsafe()
            })
        self.response.out.write(json.dumps(d))


class ListMsgs(webapp2.RequestHandler):
    def get(self):
        users =  User.query().fetch()
        d=[]
        for x in users:
            d.append({
                'text': x.text,
                'key': x.key.urlsafe()
            })
        self.response.out.write(json.dumps(d))            

class Mainpage(webapp2.RequestHandler):
    def get(self):
        def get(self):
        user = users.get_current_user()
        user_mail = user.mail()
        user_name = user.username()
        check = User.query(User.mail == user_mail).get()
        if not check:
            post_data(user_mail)
        self.redirect("/chat#!/chat")
        
             

app = webapp2.WSGIApplication([
    webapp2.Route('/', Mainpage),
    # ('/handlers/submit', Submit),
    ('/handlers/get', MsHandler),
    ('/handlers/save',MsgHandler),
     ('/handlers/submit', Submit),
    ('/handlers/ListMsgs', ListMsgs),
])