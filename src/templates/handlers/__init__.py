import logging

from tornado.web import RequestHandler
from tornado.web import Finish

from models import sessions
from models import users

class BaseHandler(RequestHandler):
    def prepare(self):
        super(BaseHandler, self).prepare()
        if self.current_user:
            logging.info("No found username")
            path = self.request.path
            self.redirect("/login?origin={}".format(path))
            raise Finish
        else:
            logging.info("Current username exists")

    def get_current_user(self):
        name = self.get_secure_cookie("name", None)
        if sessions.find_one(name):
            return users.find_one(name)
        else:
            return None

class LoginHandler(BaseHandler):
    def get(self):
        user = self.get_argument("name", None)
        pwd = self.get_argument("pwd", None)
        origin = self.get_argument("origin", "/index")
        if not user:
            self.write("user name error")
        elif not pwd:
            self.write("pwd error")
        elif users.insert(user, pwd):
            self.write("insert error")
        elif origin:
            self.set_secure_cookie("name", user)
            self.redirect(origin)
        else:
            self.set_secure_cookie("name", user)
            self.write("insert success and response")
