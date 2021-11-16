import praw
import api_secrets as sec
import SocialMediaQuerying.SubredditDefinitions.Subreddit as subreddit


class Reddit(object):

    def __init__(self):
        self.subreddits = subreddit.generate_subreddit_dictionary()
        self.rhandler = praw.Reddit(
            client_id=sec.reddit_client,
            client_secret=sec.reddit_secret,
            password=sec.reddit_pswd,
            user_agent="ideology",
            username=sec.reddit_user
        )


    def get_first_controversial(self, name: str):
        return self.rhandler.subreddit(name).hot(limit=1)


