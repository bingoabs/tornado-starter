from conf import db

COLL = db["users"]

def find_one(name):
    return COLL.find_one({"name": name})

def insert(name, pwd):
    COLL.insert({"name": name, "pwd": pwd})
