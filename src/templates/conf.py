from pymongo import MongoClient
from tornado.options import define, options


# command line params || default params
define("port", default=9096, help="app listen port")
define("db_host", default="localhost", help="mongodb host")
define("db_name", default="example", help="mongodb db name")

# database conf
db = MongoClient(host=options.db_host)[options.db_name]
port = options.port

