import argparse
from twython import Twython
from utils.functions import get_env_variables
from utils.constants import *


def main():
    parser = argparse.ArgumentParser(description='Get oauth tokens to use Twitter API.')
    parser.add_argument('-pk', '--public_key',
                        default=None,
                        type=str,
                        help='API public key.')
    parser.add_argument('-sk', '--secret_key',
                        default=None,
                        type=str,
                        help='API secret key.')
    parser.add_argument('-ef', '--env_file',
                        default=None,
                        type=str,
                        help='Environment file with variables.')

    args = parser.parse_args()
    args_dict = dict(vars(args).items())
    config = get_env_variables(
        public_key=args_dict['public_key'],
        secret_key=args_dict['secret_key'],
        env_file=args_dict['env_file']
    )

    twitter = Twython(config[PUBLIC_KEY], config[SECRET_KEY])
    authentication_tokens = twitter.get_authentication_tokens()
    print(authentication_tokens)


if __name__ == '__main__':
    main()
