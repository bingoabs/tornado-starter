import time

from conf import db

COLL = db["sessions"]

TIMEOUT = 3600 * 24 * 30 # valid until 30 days after
def find_one(name):
    record = COLL.find_one({"name": name})
    print("session record: {}".format(record))
    if not record or record["inserted_at"] < int(time.time()) - TIMEOUT:
        COLL.remove({"name": name})
        return False
    return True

def insert(name):
    COLL.insert({"name": name, "inserted_at": int(time.time())})
    return
