import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Blogasaurus.html')
        self.response.write(template.render())

class AboutMeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about_me.html')
        self.response.write(template.render())

class ContactMeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.write(template.render())

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('hello.html')
        self.response.write(template.render())

class WhyCsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('whycs.html')
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about_me.html', AboutMeHandler),
    ('/contact.html', ContactMeHandler),
    ('/hello.html', HelloHandler),
    ('/whycs.html', WhyCsHandler),
], debug=True)
