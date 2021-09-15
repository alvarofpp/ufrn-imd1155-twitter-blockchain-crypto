# Tweets about #blockchain or #crypto
[![Open in Streamlit](https://img.shields.io/badge/-Streamlit-262730?style=for-the-badge&labelColor=000000&logo=Streamlit&logoColor=white)](https://share.streamlit.io/alvarofpp/ufrn-imd1155-twitter-blockchain-crypto/main/app.py)
[![Medium](https://img.shields.io/badge/-Medium-03a57a?style=for-the-badge&labelColor=000000&logo=Medium&logoColor=white)](https://medium.com/@mvinnicius22/an%C3%A1lise-de-redes-em-um-nicho-de-conte%C3%BAdo-do-twitter-203e1cb4e31a)

This work has as purpose to analyze tweets about #blockchain and #crypto. We use [Twython](https://github.com/ryanmcgrath/twython) for download the tweets, after that we use [Streamlit](https://streamlit.io/) to make an app, you can access the app [clicking here](https://share.streamlit.io/alvarofpp/ufrn-imd1155-twitter-blockchain-crypto/main/app.py). See [this](#reproduce-this-work) section to reproduce this work.

Work of undergraduate course about Network Analysis (IMD1155) of Bachelor's degree in Information Technology from the Federal University of Rio Grande do Norte (UFRN), with [Ivanovitch Medeiros Dantas da Silva](https://github.com/ivanovitchm) as professor.

Group:
- [Álvaro Ferreira Pires de Paiva](https://github.com/alvarofpp)
  - Enrolment: 2016039162
  - E-mail: alvarofepipa@gmail.com
- [Marcos Vinícius Rêgo Freire](https://github.com/mvinnicius22)
  - Enrolment: 20210053533
  - E-mail: mvinnicius22@hotmail.com

## Requirements
The scripts are written in Python. Dependant packages can be installed via:

```shell
pip install -r requirements.txt
```

## Scripts

- Auth:
  - `auth.py` - Get auth tokens to use Twitter API.
  - `oauth.py` - Get oauth tokens to use Twitter API.
- Generate data:
  - `collect_tweets.py` - Get tweets from Twitter API.
  - `join_files.py` - Joins data files into a single CSV file.
- App:
  - `app.py` - Streamlit app.

## Reproduce this work

You need to create an app in [Twitter's Developer Platform](https://developer.twitter.com/en/portal/dashboard).

### Step 1 - Env file

Copy and paste the `.env.example` renamed to `.env`:

```shell
cp .env.example .env
```

Put your api key and secret in `PUBLIC_KEY` and `SECRET_KEY`.

### Step 2 - auth.py

Run `auth.py` providing:

| Argument | Required | Description | Default value |
| -------- | -------- | ----------- | ------------- |
| `-e` <br/> `--env_file` | No | Environment file with variables. | `.env` |

After ran the script, you will have a print of dictionary with your oauth tokens (`oauth_token` and `oauth_token_secret`) and an url to authenticate (`auth_url`).
Click in the `auth_url`, authorize the app and get the verifier code.
Put in your env file:

- `OAUTH_TOKEN`=`oauth_token`
- `OAUTH_TOKEN_SECRET`=`oauth_token_secret`
- `VERIFIER`=verifier code from `auth_url`.

Examples:
```shell
# Running the script and getting the public and secret keys from the .env file
python auth.py
```

```shell
# Running the script and specifying the env file
python auth.py -e .another.env
```

### Step 3 - oauth.py
Run `oauth.py` providing:

| Argument | Required | Description | Default value |
| -------- | -------- | ----------- | ------------- |
| `-e` <br/> `--env_file` | No | Environment file with variables. | `.env` |

After ran the script, you will have a print of dictionary with your oauth tokens (`oauth_token` and `oauth_token_secret`).
Put in your env file:

- `API_OAUTH_TOKEN`=`oauth_token`
- `API_OAUTH_TOKEN_SECRET`=`oauth_token_secret`

Examples:
```shell
# Running and getting the public and secret keys from the .env file
python oauth.py
```

```shell
# Running the script and specifying the env file
python oauth.py -e .another.env
```

### Step 4 - collect_tweets.py
You should now have all env variables filled in, which are: `PUBLIC_KEY`, `SECRET_KEY`, `API_OAUTH_TOKEN` and `API_OAUTH_TOKEN_SECRET`. Run `collect_tweets.py` providing:

| Argument | Required | Description | Default value |
| -------- | -------- | ----------- | ------------- |
| `-q` <br/> `--query` | Yes | Query to search. | - |
| `-qt` <br/> `--quantity` | No | Quantity of tweets that will be downloaded. | `1000` |
| `-e` <br/> `--env_file` | No | Environment file with variables. | `.env` |

After ran the script, you will have many CSV files in `data` folder.

Examples:
```shell
# Running the script to search tweets about #blockchain or #crypto
python collect_tweets.py -q '#blockchain OR #crypto'
```

```shell
# Running the script and specifying the env file
python collect_tweets.py -q '#blockchain OR #crypto' -e .another.env
```

```shell
# Running the script and specifying the quantity of tweets that will be downloaded
python collect_tweets.py -q '#blockchain OR #crypto' -qt 100_000
```

### Step 5 - join_files.py
Run `join_files.py` providing:

| Argument | Required | Description | Default value |
| -------- | -------- | ----------- | ------------- |
| `-o` <br/> `--output` | No | Output filename. | `"output.csv"` |

After ran the script, you will have a CSV file in `data` folder. If you intend to run the application, rename this file to `output.csv`.

Examples:
```shell
# Running script
python join_files.py
```

```shell
# Running the script and specifying the output filename
python join_files.py -o output_test.csv
```

### Step 6 - Run the app

```shell
streamlit run app.py
```

## Contributing
Contributions are more than welcome. Fork, improve and make a pull request. For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/ufrn-imd1155-twitter/issues).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
