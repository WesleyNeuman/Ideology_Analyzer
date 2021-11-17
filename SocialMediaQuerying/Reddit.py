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


class Content_Interface(object):

    def __init__(self):
        pass


class Comment(Content_Interface):
    """Content Implementation for a comment"""

    def __init__(self, comment: praw.Reddit.comment):
        self.subreddit = comment.subreddit.display_name
        self.comment_id = comment.id
        self.post_id = comment.link_id
        self.parent_id = comment.parent_id
        self.author = comment.author.name
        self.depth = comment.depth
        self.flair = comment.author_flair_text
        self.text = comment.body
        self.ups = comment.ups
        self.downs = comment.downs
        self.score = comment.score
        self.title = ''


class Post(Content_Interface):
    """Content Implementation for a post"""

    def __init__(self, post: praw.Reddit.submission):
        self.subreddit = post.subreddit
        self.comment_id = post.id
        self.post_id = post.id
        self.parent_id = 'toplevelpost'
        self.author = post.author.name
        self.depth = -1
        self.flair = post.author_flair_text
        self.text = post.selftext
        self.ups = post.ups
        self.downs = post.downs
        self.score = post.score
        self.title = post.title


def break_down_comment_tree(submission) -> list:
    """Accepts an already acquired submission object and breaks it down into individual comments"""
    submission.comments.replace_more(limit=None)
    return submission.comments.list()


