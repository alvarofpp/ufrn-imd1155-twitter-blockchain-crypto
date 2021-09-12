import itertools
from ..constants import *
from .decorators import rate_limit
from typing import Dict, List
from twython import Twython
import pandas as pd
import time


class Twitter:
    def __init__(self, config: Dict):
        self.twitter = Twython(config['PUBLIC_KEY'],
                               config['SECRET_KEY'],
                               config['API_OAUTH_TOKEN'],
                               config['API_OAUTH_TOKEN_SECRET'])
        self.rate_limit = {}
        self.total_tweets = 0
        self.last_cursor = None

    def _update_rate_limit(self) -> None:
        self.rate_limit = self.twitter.get_application_rate_limit_status()

    def _get_rate_limit(self, group: str, route: str) -> Dict:
        return self.rate_limit['resources'][group][route]

    @rate_limit(route='/search/tweets')
    def search(self,
               query: str) -> List:
        # exit(0)
        cursor = self.last_cursor
        if cursor is None:
            cursor = self.twitter.cursor(self.twitter.search, q=query, count=100, result_type='mixed')
            self.last_cursor = cursor
        return list(itertools.islice(cursor, NUM_TWEETS_TO_FETCH))

    def export(self, tweets: List):
        data = {
            'id': [],
            'name': [],
            'screen_name': [],
            'location': [],
            'followers_count': [],
            'text': [],
            'created_at': [],
            'favorite_count': [],
            'retweet_count': [],
            'lang': [],
        }

        for tweet in tweets:
            data['id'].append(tweet['user']['id'])
            data['name'].append(tweet['user']['name'])
            data['screen_name'].append(tweet['user']['screen_name'])
            data['location'].append(tweet['user']['location'])
            data['followers_count'].append(tweet['user']['followers_count'])
            data['text'].append(tweet['text'])
            data['created_at'].append(tweet['created_at'])
            data['favorite_count'].append(tweet['favorite_count'])
            data['retweet_count'].append(tweet['retweet_count'])
            data['lang'].append(tweet['lang'])

        dataframe = pd.DataFrame(data)
        current_milliseconds_time = time.time()
        filename = 'data/{}.csv'.format(str(current_milliseconds_time).replace('.', ''))
        dataframe.to_csv(filename, index=False)
        print(filename)
