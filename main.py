import webapp2
from google.appengine.ext import ndb
import json
class User(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.StringProperty()
    address = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
      def get(self):
        users =  User.query().fetch()
        d=[]
        for x in users:
            d.append({
                'name': x.name,
                'key': x.key.urlsafe()
            })
        
class Submit(webapp2.RequestHandler):
    def post(self):
        dataji =  json.loads(self.request.body)
        user = User()
        user.name = dataji.get('name')
        user.age = dataji.get('age')
        user.address = dataji.get('address')
        ref = user.put()

        users =  User.query().fetch()
        d=[]
        for x in users:
            d.append({
                'name': x.name,
                'key': x.key.urlsafe()
            })
        self.response.out.write(json.dumps(d))
class Submit1(webapp2.RequestHandler):
    def get(self):
        users =  User.query().fetch()
        d=[]
        for x in users:
            d.append({
                'name': x.name,
                'key': x.key.urlsafe()
            })
        self.response.out.write(json.dumps(d))
    
                                          
app = webapp2.WSGIApplication([
    ('/handlers/', MainPage),
    ('/handlers/submit', Submit),
    ('/handlers/get', Submit1),
])