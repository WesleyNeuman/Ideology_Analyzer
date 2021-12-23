import pymongo as mongo
import jsonpickle as jp

import api_secrets as sec
from SocialMediaQuerying.Reddit import *


class MongoLogger(object):

    def __init__(self, collection):
        self.client = mongo.MongoClient('localhost', 27107)
        self.database = self.client['ideology']
        self.collection = self.database[collection]


def mongo_log_helper(mlogger: MongoLogger, documents: dict):
    # Check existence of ids
    mlogger.collection.find(filter={"_id" : {dict.keys}}, projection={"_id" : 1})

    # Separate document list into existing ids and new ids

    # Replace existing ids

    # Insert new ids
    pass


def log_documents_from_reddit_post(mlogger: MongoLogger, content: dict):
    doculist = []
    for value in content.values():
        doculist.append(jp.encode(value))
    mlogger.collection.insert_many(doculist)


