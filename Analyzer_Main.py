# Import External Modules
import pandas as pd
import nltk
import jsonpickle as jp

import logging, os

# Import Internal Modules
import Analysis.PostSentimentChain as psc
import Analysis.WordPreprocessing as wp
import Analysis.WesleyHeuristics as wh
from SocialMediaQuerying.Reddit import *
import MongoDB.LoggingMongo as logmongo

# Setup
if os.path.exists('MasterTestingDebug.log'):
    os.remove('MasterTestingDebug.log')
logging.basicConfig(filename='MasterTestingDebug.log', level=logging.INFO)
mlogger = logmongo.MongoLogger

# Testing code for getting a post from reddit
reddit = Reddit()

sublist = reddit.rhandler.subreddit('atheism').hot(limit=1)
post_breakdown = []
for post in sublist:
    post_breakdown.append(create_dict_from_post(post))

post = post_breakdown[0]

# Testing code for calling analysis
post = psc.reddit_post_sentiment_difference_from_parent(post)
doculist = logmongo.log_documents_from_reddit_post(post)
doculist2 = []
for i in range(len(doculist)):
    doculist2.append(jp.decode(doculist[i]))

print(vars(doculist2[0]))

# Testing code for logging analyzed data
#logger = awslog.DynamoLogger()


