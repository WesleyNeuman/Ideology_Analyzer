# Import External Modules
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Import Internal Modules
from SocialMediaQuerying.Reddit import *


def reddit_post_sentiment(post: dict) -> dict:
    """Finds the sentiment of every item in a post"""
    sa = SentimentIntensityAnalyzer()
    for i in post:
        if 'TextSentiment' not in post[i].analyses:
            post[i].analyses['TextSentiment'] = sa.polarity_scores(post[i].text)
    return post


def reddit_post_sentiment_difference_from_parent(post: dict) -> dict:
    """Finds the difference in sentiment scores between an item and its parent, dependent on reddit_post_sentiment"""
    post = reddit_post_sentiment(post)

    # Have parent search for children, not children search for parent

    #
    pass


