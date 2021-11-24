from SocialMediaQuerying.SubredditDefinitions import Categorizations as cat


class Subreddit(object):
    """Contains my properties for grouping subreddits"""
    def __init__(self, name: str, category: cat.Category, humor: cat.Humor):
        self.name = name
        self.category = category
        self.humor = humor


def generate_subreddit_dictionary() -> dict:
    subdict = {}
    humor = cat.Humor
    category = cat.Category

    subdict['PoliticalCompassMemes'] = Subreddit('PoliticalCompassMemes', category.POLITICAL, humor.FUNNY)
    subdict['Conservative'] = Subreddit('Conservative', category.POLITICAL, humor.SERIOUS)
    subdict['atheism'] = Subreddit('atheism', category.RELIGIOUS, humor.SERIOUS)
    subdict['BlackPeopleTwitter'] = Subreddit('BlackPeopleTwitter', category.RACIAL, humor.MIXED)

    return subdict



