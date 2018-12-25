from handlers import LoginHandler
from handlers.index import IndexHandler

handlers = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/index", IndexHandler)
]
