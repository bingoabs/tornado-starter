import logging

from tornado.web import RequestHandler
from tornado.web import Finish

from models import sessions
from models import users

class BaseHandler(RequestHandler):
    def prepare(self):
        super(BaseHandler, self).prepare()
        logging.info(self.current_user)
        if self.current_user:
            logging.info("Current username exists")
        else:
            logging.info("Current username not found")
            path = self.request.path
            self.redirect("/login?origin={}".format(path))
            raise Finish

    def get_current_user(self):
        name = self.get_secure_cookie("name", None)
        logging.info("Current cookie: {}".format(name))
        if sessions.find_one(name):
            return users.find_one(name)
        else:
            return None

class LoginHandler(RequestHandler):
    def get(self):
        name = self.get_query_argument("name", None)
        pwd = self.get_query_argument("pwd", None)
        if None in [name, pwd]:
            self.write("name or pwd error")
            return
        self.set_secure_cookie("name", name)
        users.insert(name, pwd)
        sessions.insert(name)

        origin = self.get_query_argument("origin", "/index")
        if origin:
            self.redirect(origin)
        else:
            self.write("insert success and response")
