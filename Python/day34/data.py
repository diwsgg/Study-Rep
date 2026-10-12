import requests

necessary_params={
    'amount' : 10,
    'type' : 'boolean',
}

response = requests.get(url='https://opentdb.com/api.php', params=necessary_params)
response.raise_for_status()

data_questions = response.json()['results']
