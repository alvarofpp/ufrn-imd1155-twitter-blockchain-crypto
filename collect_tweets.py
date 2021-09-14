import argparse
from utils.twitter import Twitter
from utils.functions import get_env_variables


def main():
    parser = argparse.ArgumentParser(description='Get tweets from Twitter API.')
    parser.add_argument('-q', '--query',
                        required=True,
                        type=str,
                        help='Query to search.')
    parser.add_argument('-qt', '--quantity',
                        default=1000,
                        type=str,
                        help='Quantity of tweets that will be downloaded.')
    parser.add_argument('-e', '--env_file',
                        default='.env',
                        type=str,
                        help='Environment file with variables.')

    args = parser.parse_args()
    args_dict = dict(vars(args).items())
    config = get_env_variables(
        keys=[
            'PUBLIC_KEY',
            'SECRET_KEY',
            'API_OAUTH_TOKEN',
            'API_OAUTH_TOKEN_SECRET',
        ],
        env_file=args_dict['env_file']
    )

    twitter = Twitter(config)
    quantity = int(args_dict['quantity'])

    while twitter.total_tweets < quantity:
        search_tweets = twitter.search(query=args_dict['query'])
        twitter.export(search_tweets)
        twitter.total_tweets += len(search_tweets)


if __name__ == '__main__':
    main()
