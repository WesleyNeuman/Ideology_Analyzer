import pymongo as mongo
import jsonpickle as jp

import api_secrets as sec
from SocialMediaQuerying.Reddit import *


class MongoLogger(object):

    def __init__(self, collection):
        self.client = mongo.MongoClient('localhost', 27107)
        self.database = self.client['ideology']
        self.collection = self.database[collection]


def log_document(mlogger: MongoLogger, documents):
    mlogger.collection.insert_many(documents)


def build_documents_from_reddit_post(content: dict):
    doculist = []
    for value in content.values():
        doculist.append(jp.encode(value))
    return doculist


