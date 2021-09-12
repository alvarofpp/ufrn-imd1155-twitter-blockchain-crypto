import itertools
from ..constants import *
from typing import Dict
from twython import Twython


class Twitter:
    def __init__(self, config: Dict):
        self.twitter = Twython(config['PUBLIC_KEY'],
                               config['SECRET_KEY'],
                               config['API_OAUTH_TOKEN'],
                               config['API_OAUTH_TOKEN_SECRET'])
        self.data = {}

    def search(self,
               query: str):
        cursor = self.twitter.cursor(self.twitter.search, q=query, count=100, result_type='mixed')
        search_tweets = list(itertools.islice(cursor, NUM_TWEETS_TO_FETCH))
        print(len(search_tweets))
