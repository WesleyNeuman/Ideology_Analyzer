# The goal of this demonstration program is to take a collection of posts from a plethora of subreddits,
# perform sentiment analysis on the post content as well as all of the comments, perform exploratory analysis
# on the sentiment scores, and then log the results to a dev SQL Server instance. Then this data can be called
# into PowerBI or Excel for demonstration of use to Heartland

# Import External Modules
import pyodbc

# Import Internal Modules
import Analysis.PostSentimentChain as psc
import api_secrets
from SocialMediaQuerying.Reddit import *

# Setup
reddit = Reddit()

# Get current top 100 posts and create breakdown
sublist = reddit.rhandler.subreddit('popular').hot(limit=15)
post_breakdown = []
for post in sublist:
    print(post.num_comments)
    if post.num_comments < 1000:
        post_breakdown.append(create_dict_from_post(post))

# Calculate sentiment scores
for i in range(0, len(post_breakdown)):
    print("breaking down...")
    post_breakdown[i] = psc.reddit_post_sentiment_difference_from_parent(post_breakdown[i])



# Log data to MSSQL
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=localhost\\MSSQLSERVER01;Database=RedditSentimentDemo;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("""DELETE FROM dbo.SentimentScores""")
conn.commit()

for post in post_breakdown:
    for key, item in post.items():
        if item.parent_id != 'toplevelpost':
            cursor.execute("""INSERT INTO dbo.SentimentScores (ItemID, PostOrComment, PositiveScore, NeutralScore, NegativeScore, CompositeScore, ParentDifPositive, ParentDifNeutral, ParentDifNegative, ParentDifComposite, PostID, Subreddit, ParentID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                           item.comment_id, None, item.analyses['TextSentiment']['pos'], item.analyses['TextSentiment']['neu'], item.analyses['TextSentiment']['neg'], item.analyses['TextSentiment']['compound'],
                           item.analyses['TextSentimentParentDifferences']['pos'], item.analyses['TextSentimentParentDifferences']['neu'], item.analyses['TextSentimentParentDifferences']['neg'],
                           item.analyses['TextSentimentParentDifferences']['compound'], item.post_id, item.subreddit, item.parent_id
                           )
        else:
            cursor.execute(
                """INSERT INTO dbo.SentimentScores (ItemID, PostOrComment, PositiveScore, NeutralScore, NegativeScore, CompositeScore, ParentDifPositive, ParentDifNeutral, ParentDifNegative, ParentDifComposite, PostID, Subreddit, ParentID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                item.comment_id, None, item.analyses['TextSentiment']['pos'], item.analyses['TextSentiment']['neu'],
                item.analyses['TextSentiment']['neg'], item.analyses['TextSentiment']['compound'],
                None, None, None, None, item.post_id, item.subreddit, item.parent_id
                )

cursor.commit()






