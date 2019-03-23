from flask import Flask, render_template
import math
import requests
import json
app = Flask(__name__)

ONEMAP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI1MTksInVzZXJfaWQiOjI1MTksImVtYWlsIjoiYm9rd29vbi5jQGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1MzM0MTc4NywiZXhwIjoxNTUzNzczNzg3LCJuYmYiOjE1NTMzNDE3ODcsImp0aSI6IjU2ZWI1YmRkZjBjMDkwNWNkZWNmMWNkYzBmNTViYjY0In0.r7M2SMKECiSdMdSNcuqO8JIQcV9JeE4YIwe56pIW_iA"


def retrieve_carpark_list():
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&limit=5'
    Jlist = requests.get(url).json()


def user_location():
    postal_code = input()
    domain = "https://developers.onemap.sg/commonapi/search?searchVal="
    options = "&returnGeom=Y&getAddrDetails=N"
    # print(requests.get(domain + postal_code + options).json())
    r = requests.get(domain + postal_code + options).json()['results'][0]
    return (r['X'], r['Y'])


def find_nearest(a={"x": 11745, "y": 36284}):
    with open('data.json') as f:
        carpark_list = json.load(f)
    listt = []
    for b in carpark_list:
        x = float(b['x'])
        y = float(b['y'])
        carpark = b['carpark_number']
        listt.append((math.hypot(a['x'] - x, a['y'] - y), carpark, (x, y)))
    print(min(listt))


def route(start_lat, start_long, end_lat, end_long): #function not done
    domain = 'https://developers.onemap.sg/privateapi/routingsvc/route?start='
    start = '1.319728,103.8421'
    '&end='
    end = '1.319728905,103.8421581'
    '&routeType=drive&token=' + ONEMAP_TOKEN


def check_lots():
    loturl = 'https://api.data.gov.sg/v1/transport/carpark-availability'
    requests.get(loturl).json()


def svy_to_wgs(X, Y):
    url = 'https://developers.onemap.sg/commonapi/convert/3414to4326?'
    params = 'X=' + str(X) + '&Y=' + str(Y)

    print(requests.get(url + params).json())


def maproute():
    "<iframe src='https://tools.onemap.sg/amm/amm.html?&marker=latLng:1.37219780826066,103.901539947637!colour:lightgreen&marker=latLng:1.29586084756524,103.77873796155!colour:red!rType:TRANSIT!rDest:1.37219780826066,103.901539947637&zoomLevl=13&popupWidth=200&popupHeight=500&design=Default' height=450px width=450px scrolling='no' frameborder='0' allowfullscreen='allowfullscreen'></iframe>"


requests.get('https://developers.onemap.sg/commonapi/convert/3414to4326?X=20134.1254&Y=40120.981').json()

requests.get('https://developers.onemap.sg/commonapi/convert/3414to4326?X=11745&Y=36284').json()


def main():
    geom = user_location()
    # print(geom) #prints user_location X&Y
    # convert_svy_to_wgs(geom[0], geom[1]) #test conversion function
    # find_nearest(user_location())
    check_lots()


@app.route('/')
def hello_world():
    return '<h1>ttt</h1>'
