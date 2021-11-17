# Import External Modules
import pandas as pd
import PandasWrappers as pw
import AWS.Logging as awslog
import pprint

# Import Internal Modules
import SocialMediaQuerying.Reddit as Reddit


reddit = Reddit.Reddit()
#logger = awslog.DynamoLogger()

sublist = reddit.rhandler.subreddit('funny').hot(limit=1)
comment_list = []
for post in sublist:
    comment_list = reddit.break_down_comment_tree(post)

pprint.pprint(vars(comment_list[0]))