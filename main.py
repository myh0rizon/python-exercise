import json
import os
import requests
from utils.sql import check_record_exists
from libs.odds import create_record


def main():

    # fetch api key from env var
    api_key = os.environ.get('ODDS_API_KEY')

    if api_key is None:
        print("Cannot get api key from ODDS_API_KEY environment variable")
        return

    # set sport to "upcoming" to see live and upcoming across all sports OR
    # use particular field, example: soccer_netherlands_eredivisie
    sport_key = 'upcoming'

    # api request param to filter data
    req_params = {
        'api_key': api_key,
        'sport': sport_key,
        'region': 'uk',
        'mkt': 'h2h'
    }

    # make http request to get odds data using param data filter
    api_response = requests.get('https://api.the-odds-api.com/v3/odds', req_params)

    # convert api_response from json
    api_response_json = json.loads(api_response.text)

    # check if request was successful
    if not api_response_json['success']:
        print(
            'There was a problem with the request:',
            api_response_json['msg']
        )
        return

    # iterate through events and save new records to db
    for idx in range(len(api_response_json['data'])):

        id = api_response_json['data'][idx]['id']
        sport_key = api_response_json['data'][idx]['sport_key']
        sport_nice = api_response_json['data'][idx]['sport_nice']
        team_a = api_response_json['data'][idx]['teams'][0]
        team_b = api_response_json['data'][idx]['teams'][1]
        home_team = api_response_json['data'][idx]['home_team']
        commence_time = api_response_json['data'][idx]['commence_time']

        record_exists = check_record_exists('betting', 'odds', id)

        print(f'Record with ID {id} exists >> ', record_exists)

        if not record_exists:
            record_created = create_record(
                id,
                sport_key,
                sport_nice,
                team_a,
                team_b,
                home_team,
                commence_time)

            print(f'Rcord with ID {id} save successful >> ', record_created)

    # Check API usage
    print('Remaining API requests', api_response.headers['x-requests-remaining'])
    print('Used API requests', api_response.headers['x-requests-used'])


if __name__ == "__main__":
    main()
