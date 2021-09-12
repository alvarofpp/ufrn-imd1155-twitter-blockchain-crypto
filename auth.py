import argparse
from twython import Twython
from utils.functions import get_env_variables


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

    config = {}
    public_key = args_dict['public_key']
    secret_key = args_dict['secret_key']

    if (public_key is None and secret_key is not None) \
            or (public_key is not None and secret_key is None):
        raise Exception('You must declare the public and secret key together.')

    if public_key and secret_key:
        config = {
            'PUBLIC_KEY': public_key,
            'SECRET_KEY': secret_key,
        }

    if not bool(config):
        config = get_env_variables(
            keys=[
                'PUBLIC_KEY',
                'SECRET_KEY',
            ],
            env_file=args_dict['env_file']
        )

    twitter = Twython(config['PUBLIC_KEY'], config['SECRET_KEY'])
    authentication_tokens = twitter.get_authentication_tokens()
    print(authentication_tokens)


if __name__ == '__main__':
    main()
