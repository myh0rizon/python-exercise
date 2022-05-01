# python-exercise

## Prep steps

Create virtual environment `pipenv install`

Execute into environment: `pipenv shell`

Get your API key from: https://the-odds-api.com/#get-access

Create the odds API key env var: `export ODDS_API_KEY=[YOUR_API_KEY_VALUE]`

Create local sqlite3 DB: `pipenv run python utils/create_odds_table.py`

## Commands

Run the app: `pipenv run python main.py`

Code quality: `pipenv run pylama`

## Utils

Check local db records: `pipenv run python utils/check_odds_table.py`