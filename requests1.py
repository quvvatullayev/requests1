import requests
import json
from pprint import pprint

def get_info(d):
    first = d['name']['first']
    last = d['name']['last']
    age = d['registered']['age']
    gender = d['gender']
    country = d['location']['country']

    data = {
                'first_name':first,
                'last_name':last,
                'age':age,
                'country':country,
                'gender':gender

            }

    return data

def print_def(n = 10):
    results = []
    for i in range(n):
        r = requests.get('https://randomuser.me/api/')
        if r.status_code == 200:
            h = r.json()
            d = h['results'][0]
            x = get_info(d)
            results.append(x)
        else:
            print(f"Requests status_code : {r.status_code}")
    dict1 = {'results':results}
    return dict1

requests1 = print_def()
with open('requests.json', 'w') as f:
    json.dump(requests1, f, indent=2)
