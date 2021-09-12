from time import sleep
from datetime import datetime


def rate_limit(route: str):
    if route[0] != '/':
        route = '/' + route

    group = route.split('/')[1]

    def wrapper(func):
        def call(*args, **kwargs):
            self = args[0]
            self._update_rate_limit()
            rate_limit_data = self._get_rate_limit(group, route)
            if rate_limit_data['remaining'] < 10:
                datetime_reset = datetime.fromtimestamp(int(rate_limit_data['reset']))
                now = datetime.now()
                seconds = int((datetime_reset - now).total_seconds() + 1)
                print('SLEEP for {} seconds.'.format(seconds))
                sleep(seconds)

            return func(*args, **kwargs)
        return call
    return wrapper
