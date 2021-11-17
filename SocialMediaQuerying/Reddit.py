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


    def break_down_comment_tree(self, submission) -> list:
        """Accepts an already acquired submission object and breaks it down into individual comments"""
        submission.comments.replace_more(limit=None)
        return submission.comments.list()


