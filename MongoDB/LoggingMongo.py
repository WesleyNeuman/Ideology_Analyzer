import pymongo as mongo
import api_secrets as sec

class MongoLogger(object):

    def __init__(self):
        self.client = mongo.MongoClient('hostname', 27107)
