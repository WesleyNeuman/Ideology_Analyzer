# Import External Modules
import pandas as pd
import WesleysPythonToolkit.PandasWrappers as pw
import pprint

# Import Internal Modules
from SocialMediaQuerying.Reddit import *
import AWS.LoggingAWS as logaws
import MongoDB.LoggingMongo as logmongo

# Testing code for getting a post from reddit
reddit = Reddit()

sublist = reddit.rhandler.subreddit('atheism').hot(limit=1)
post_breakdown = []
for post in sublist:
    post_breakdown.append(Post(post=post))
print(logmongo.build_documents_from_reddit_post(post_breakdown[0]))

# Testing code for calling analysis


# Testing code for logging analyzed data
#logger = awslog.DynamoLogger()


