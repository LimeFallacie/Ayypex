from flask import Flask, render_template, request
import math
import requests
import json
app = Flask(__name__)

ONEMAP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI1MTksInVzZXJfaWQiOjI1MTksImVtYWlsIjoiYm9rd29vbi5jQGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1MzM0MTc4NywiZXhwIjoxNTUzNzczNzg3LCJuYmYiOjE1NTMzNDE3ODcsImp0aSI6IjU2ZWI1YmRkZjBjMDkwNWNkZWNmMWNkYzBmNTViYjY0In0.r7M2SMKECiSdMdSNcuqO8JIQcV9JeE4YIwe56pIW_iA"


def addr_to_svy(addr):
    """
    converts an andress to the svy21 format
    """
    domain = "https://developers.onemap.sg/commonapi/search?searchVal="
    options = "&returnGeom=Y&getAddrDetails=N"
    r = requests.get(domain + addr + options).json()['results'][0]
    return (float(r['X']), float(r['Y']))


# def find_nearest(a={"x": 11745, "y": 36284}):
def find_nearest(ax, ay):
    with open('data.json') as f:
        carpark_list = json.load(f)
    biglist = []
    for b in carpark_list:
        xb = float(b['x'])
        yb = float(b['y'])
        carpark = b['carpark_number']
        biglist.append((math.hypot(ax - xb, ay - yb), carpark, xb, yb))
        lots = 555
    r = min(biglist)
    return (r[2], r[3], lots)


def check_lots():
    loturl = 'https://api.data.gov.sg/v1/transport/carpark-availability'
    requests.get(loturl).json()


def svy_to_wgs(X, Y):
    url = 'https://developers.onemap.sg/commonapi/convert/3414to4326?'
    params = 'X=' + str(X) + '&Y=' + str(Y)
    r = requests.get(url + params).json()
    return str(r['latitude']) + "," + str(r['longitude'])


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        xa, ya = addr_to_svy(request.form['address'])
        start = svy_to_wgs(xa, ya)
        xb, yb, lots = find_nearest(xa, ya)
        end = svy_to_wgs(xb, yb)
    else:
        start = "1.37219780826066,103.901539947637"
        end = "1.37219780826066,103.901539947637"
        lots = 555
    return render_template('index.html', start=start, end=end, lots=lots)
