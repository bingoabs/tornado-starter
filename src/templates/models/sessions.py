from conf import db

COLL = db["sessions"]

def find_one(username):
    return COLL.find_one({"username": username})