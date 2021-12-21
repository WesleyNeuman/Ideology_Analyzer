# Import External Modules
import pandas as pd
import WesleysPythonToolkit.PandasWrappers as pw
import nltk

import logging, os

# Import Internal Modules
import Analysis.PostSentimentChain as psc
import Analysis.WordPreprocessing as wp
import Analysis.WesleyHeuristics as wh
from SocialMediaQuerying.Reddit import *
import AWS.LoggingAWS as logaws
import MongoDB.LoggingMongo as logmongo

# Setup
if os.path.exists('MasterTestingDebug.log'):
    os.remove('MasterTestingDebug.log')
logging.basicConfig(filename='MasterTestingDebug.log', level=logging.INFO)

# Testing code for getting a post from reddit
reddit = Reddit()

sublist = reddit.rhandler.subreddit('atheism').hot(limit=1)
post_breakdown = []
for post in sublist:
    post_breakdown.append(create_dict_from_post(post))

post = post_breakdown[0]

# Testing code for calling analysis
post = psc.reddit_post_sentiment(post)
for item in post.values():
    print(item.analyses['TextSentiment'])

# Testing code for logging analyzed data
#logger = awslog.DynamoLogger()


