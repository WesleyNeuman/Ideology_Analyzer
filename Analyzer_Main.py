# Import External Modules
import pandas as pd
import WesleysPythonToolkit.PandasWrappers as pw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

import logging, os

# Import Internal Modules
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
    post_breakdown.append(Post(post=post))

post = post_breakdown[0]
print(post.title)

# Testing code for calling analysis

sentiment = SentimentIntensityAnalyzer()
print(sentiment.polarity_scores(post.title))
for comment in post.comment_list:
    print(comment.text)
    print(sentiment.polarity_scores((comment.text)))

# Testing code for logging analyzed data
#logger = awslog.DynamoLogger()


