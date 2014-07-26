import os
import jinja2
import webapp2
from model.models import *


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/views"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Index(webapp2.RequestHandler):

    def get(self):
        selector = ndb.gql("SELECT * FROM Project")
        template_values = { 'projects': selector }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Show(webapp2.RequestHandler):
    def get(self):
        id = self.request.get('id')
        project = Project.get_by_id(int(id))
        template_values = {
            'name': project.name,
            'img_url': project.img_url,
            'description': project.description,
            'author': project.author,
            'url': project.url
        }
        template = JINJA_ENVIRONMENT.get_template('show.html')
        self.response.write(template.render(template_values))


class New(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('new.html')
        self.response.write(template.render())

    def post(self):
        self.project = Project(name = self.request.get('name'),
                               img_url = self.request.get('img_url'),
                               description = self.request.get('description'),
                               author = self.request.get('author'),
                               url = self.request.get('url'))
        self.project.put()
        self.redirect('/')


class Edit(webapp2.RequestHandler):

    def get(self):
        id = self.request.get('id')
        project = Project.get_by_id(int(id))
        template_values = {
            'name': project.name,
            'img_url': project.img_url,
            'description': project.description,
            'author': project.author,
            'url': project.url
        }
        template = JINJA_ENVIRONMENT.get_template('edit.html')
        self.response.write(template.render(template_values))

    def post(self):
        id = self.request.get('id')
        self.project = Project(id = int(id),
                               name = self.request.get('name'),
                               img_url = self.request.get('img_url'),
                               description = self.request.get('description'),
                               author = self.request.get('author'),
                               url = self.request.get('url'))
        self.project.put()
        self.redirect('/')

class Destroy(webapp2.RequestHandler):

    def get(self):
        id = self.request.get('id')
        self.project = Project(id = int(id))
        ndb.delete_multi([self.project.key])
        self.redirect('/')


application = webapp2.WSGIApplication([
    ('/', Index),
    ('/show', Show),
    ('/new', New),
    ('/edit', Edit),
    ('/destroy', Destroy)
], debug=True)