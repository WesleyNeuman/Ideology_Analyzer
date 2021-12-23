import pymongo as mongo
import logging


class MongoGetter(object):

    def __init__(self, collection):
        self.client = mongo.MongoClient('localhost', 27107)
        self.database = self.client['ideology']
        self.collection = self.database[collection]

def get_mongo(mongodef: MongoGetter, keys: list, values: list) -> list:
    """Builds a query dictionary based on the keys and values provided"""
    try:
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = str(values[i])
        return mongodef.collection.find(filter=dict)
    except Exception as inst:
        logging.error(inst)


def get_reddit_post_documents():
    pass
