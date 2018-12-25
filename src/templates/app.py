#!/usr/bin/python
# coding:utf-8
import logging
from os import path
# something the logging level change!
logging.getLogger().setLevel(logging.INFO)

from tornado.ioloop import IOLoop
from tornado.web import Application

from conf import port
from urls import handlers

root = path.dirname(__file__)
kwargs = {
    "autoreload": True,
    "debug": True,
    "cookie_secret": "0e9133e506744318af3bdc5a3f8ed726",
    "login_url": "/login",
    "xsrf_cookies": True,
    "template_path": path.join(root, "templates"),
    "static_path": path.join(root, "statics")
}

if __name__ == "__main__":
    app = Application(handlers, **kwargs)
    app.listen(port)
    logging.info("start app at port: {}".format(port))
    IOLoop.current().start()
