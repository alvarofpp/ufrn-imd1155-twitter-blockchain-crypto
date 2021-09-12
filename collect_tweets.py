import argparse
from utils.twitter import Twitter
from utils.functions import get_env_variables


def main():
    parser = argparse.ArgumentParser(description='Get tweets from Twitter API.')
    parser.add_argument('-q', '--query',
                        required=True,
                        type=str,
                        help='Query to search.')
    parser.add_argument('-o', '--output',
                        required=True,
                        type=str,
                        help='Query to search.')
    parser.add_argument('-pk', '--public_key',
                        default=None,
                        type=str,
                        help='API public key.')
    parser.add_argument('-sk', '--secret_key',
                        default=None,
                        type=str,
                        help='API secret key.')
    parser.add_argument('-ot', '--oauth_token',
                        default=None,
                        type=str,
                        help='Oauth token.')
    parser.add_argument('-ots', '--oauth_token_secret',
                        default=None,
                        type=str,
                        help='Oauth token secret.')
    parser.add_argument('-ef', '--env_file',
                        default=None,
                        type=str,
                        help='Environment file with variables.')

    args = parser.parse_args()
    args_dict = dict(vars(args).items())

    config = {
        'PUBLIC_KEY': args_dict['public_key'],
        'SECRET_KEY': args_dict['secret_key'],
        'API_OAUTH_TOKEN': args_dict['oauth_token'],
        'API_OAUTH_TOKEN_SECRET': args_dict['oauth_token_secret'],
    }
    config = {key: value for key, value in config.items() if value}
    keys = [
        'PUBLIC_KEY',
        'SECRET_KEY',
        'API_OAUTH_TOKEN',
        'API_OAUTH_TOKEN_SECRET',
    ]
    missing_keys = list(set(keys).difference(set(config.keys())))

    if len(missing_keys) > 0:
        missing_config = get_env_variables(
            keys=missing_keys,
            env_file=args_dict['env_file']
        )
        config = {**missing_config, **config}

    twitter = Twitter(config)
    twitter.search(query=args_dict['query'])


if __name__ == '__main__':
    main()
