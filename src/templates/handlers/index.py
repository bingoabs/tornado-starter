import logging

from handlers import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        logging.info("Index handler receive request")
        self.write("Hello success")