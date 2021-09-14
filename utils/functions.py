from typing import Dict, List
from dotenv import dotenv_values


def get_env_variables(keys: List,
                      env_file: str) -> Dict:
    config = dotenv_values(env_file)

    if not bool(config):
        raise Exception('environment variables file is empty or not exist')

    for key in keys:
        if key not in config.keys():
            raise Exception('You must have {} in your environment variables file'.format(key))

        if not config[key]:
            raise Exception('{} cannot be None or empty'.format(key))

    return config
