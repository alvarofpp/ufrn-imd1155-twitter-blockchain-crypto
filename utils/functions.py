from .constants import *
from typing import Dict
from dotenv import dotenv_values


def get_env_variables(public_key: str = None,
                      secret_key: str = None,
                      env_file: str = None) -> Dict:
    if (public_key is None and secret_key is not None) \
            or (public_key is not None and secret_key is None):
        raise Exception('You must declare the public and secret key together.')

    if public_key and secret_key:
        return {
            PUBLIC_KEY: public_key,
            SECRET_KEY: secret_key,
        }

    filename = env_file if env_file else '.env'
    config = dotenv_values(filename)

    if not bool(config):
        raise Exception('environment variables file is empty or not exist')

    keys = [
        PUBLIC_KEY,
        SECRET_KEY,
    ]

    for key in keys:
        if key not in config.keys():
            raise Exception('You must have {} in your environment variables file'.format(key))

        if not config[key]:
            raise Exception('{} cannot be None or empty'.format(key))

    return config
