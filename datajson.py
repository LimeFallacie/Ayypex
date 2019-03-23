import requests
import json
url = 'https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c'

rs = requests.get(url).json()['result']['records']

l = []
for r in rs:
    d = {}
    d['carpark_number'] = r['car_park_no']
    d['x'] = r['x_coord']
    d['y'] = r['y_coord']
    l.append(d)

with open('data.json', 'w') as fp:
    json.dump(l, fp)
