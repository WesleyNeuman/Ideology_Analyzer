# Import External Modules
import pandas as pd
import PandasWrappers as pw
import AWS.Logging as awslog
import pprint

# Import Internal Modules
from SocialMediaQuerying.Reddit import *

# Testing code for getting a post from reddit
reddit = Reddit()

sublist = reddit.rhandler.subreddit('atheism').hot(limit=1)
post_breakdown = []
for post in sublist:
    post_breakdown.append(Post(post=post))
    comment_list = break_down_comment_tree(post)
    for comment in comment_list:
        post_breakdown.append(Comment(comment=comment))

# Testing code for calling analysis


# Testing code for logging analyzed data
#logger = awslog.DynamoLogger()


