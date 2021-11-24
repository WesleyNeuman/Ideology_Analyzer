import pymongo as mongo

import api_secrets as sec
from SocialMediaQuerying.Reddit import *


class MongoLogger(object):

    def __init__(self, collection):
        self.client = mongo.MongoClient('localhost', 27107)
        self.database = self.client['ideology']
        self.collection = self.database[collection]


def log_document(mlogger: MongoLogger, documents):
    mlogger.collection.insert_many(documents)


def build_documents_from_reddit_post(content: Post):
    doculist = []
    for comment in content.comment_list:
        doculist.append(vars(comment))
    temp = vars(content)
    del temp['comment_list']
    doculist.append(temp)
    return doculist


