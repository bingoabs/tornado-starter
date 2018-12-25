from os import path
from tornado.ioloop import IOLoop
from tornado.web import Application

from conf import port
from urls import handlers

root = path.dirname(__file__)
kwargs = {
    "cookie_secret": "0e9133e506744318af3bdc5a3f8ed726",
    "login_url": "/login",
    "xsrf_cookies": True,
    "template_path": path.join(root, "templates"),
    "static_path": path.join(root, "statics")
}

if __name__ == "__main__":
    app = Application(handlers, **kwargs)
    app.listen(port)
    IOLoop.current().start()
