from google.appengine.ext import ndb

class Project(ndb.Model):
  name = ndb.StringProperty(indexed=False)
  img_url = ndb.StringProperty(indexed=False)
  description = ndb.StringProperty(indexed=False)
  author = ndb.StringProperty(indexed=False)
  url = ndb.StringProperty(indexed=False)