import argparse
from twython import Twython
from utils.functions import get_env_variables


def main():
    parser = argparse.ArgumentParser(description='Get final oauth tokens to use Twitter API.')
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
            'OAUTH_TOKEN',
            'OAUTH_TOKEN_SECRET',
            'VERIFIER',
        ],
        env_file=args_dict['env_file']
    )

    twitter = Twython(config['PUBLIC_KEY'],
                      config['SECRET_KEY'],
                      config['OAUTH_TOKEN'],
                      config['OAUTH_TOKEN_SECRET'])

    authorized_tokens = twitter.get_authorized_tokens(config['VERIFIER'])
    print(authorized_tokens)


if __name__ == '__main__':
    main()
