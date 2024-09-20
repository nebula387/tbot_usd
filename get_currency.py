import requests
from pprint import pprint

currency = ['RUR', 'USD', 'BYR', 'EUR', 'KZT']


def get_cur(cur):
    # currency = ['RUR', 'USD', 'BYR', 'EUR', 'KZT']
    result = requests.get(f'https://open.er-api.com/v6/latest/USD')
    data = result.json()
    rat = data['rates']
    dict_cur = {}
    for c in cur:
        if c in rat:
            result = requests.get(f'https://open.er-api.com/v6/latest/{c}')
            data = result.json()
            r = data['rates']['RUB']
            dict_cur[c] = r
    return dict_cur


print(get_cur(currency))
