import requests
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
        h = r.json()
        d = h['results'][0]
        x = get_info(d)
        results.append(x)
    dict1 = {'results':results}
    return dict1

requests1 = print_def()
pprint(requests1)


