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


class Comment(object):
    """Selects my desired content from a reddit comment"""

    def __init__(self, comment: praw.Reddit.comment):
        self._id = 'r_' + str(comment.id)
        self.subreddit = str(comment.subreddit.display_name)
        self.comment_id = str(comment.id)
        self.post_id = str(comment.link_id)
        self.parent_id = str(comment.parent_id)
        self.author = str(comment.author.name)
        self.depth = str(comment.depth)
        self.flair = str(comment.author_flair_text)
        self.text = str(comment.body)
        self.ups = str(comment.ups)
        self.downs = str(comment.downs)
        self.score = str(comment.score)
        self.title = ''


class Post(object):
    """Creates a post object by selecting data I want out of the reddit submission along with creating objects from each of the comments"""

    def __init__(self, post: praw.Reddit.submission):
        self._id = 'r_' + str(post.id)
        self.subreddit = str(post.subreddit.display_name)
        self.comment_id = str(post.id)
        self.post_id = str(post.id)
        self.parent_id = 'toplevelpost'
        self.author = str(post.author.name)
        self.depth = '-1'
        self.flair = str(post.author_flair_text)
        self.text = str(post.selftext)
        self.ups = str(post.ups)
        self.downs = str(post.downs)
        self.score = str(post.score)
        self.title = str(post.title)
        self.comment_list = process_comments(post)


def process_comments(post):
    """Creates list of comment objects from a post"""
    comments = break_down_comment_tree(post)
    comment_obj_list = []
    for comment in comments:
        if comment.author != None:
            comment_obj_list.append(Comment(comment=comment))
    return comment_obj_list


def break_down_comment_tree(submission) -> list:
    """Accepts an already acquired submission object and breaks it down into individual comments"""
    submission.comments.replace_more(limit=None)
    return submission.comments.list()







