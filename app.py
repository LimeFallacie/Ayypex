from flask import Flask, render_template, request, jsonify
import math
import requests
import json
app = Flask(__name__)

ONEMAP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI1MTksInVzZXJfaWQiOjI1MTksImVtYWlsIjoiYm9rd29vbi5jQGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1MzM0MTc4NywiZXhwIjoxNTUzNzczNzg3LCJuYmYiOjE1NTMzNDE3ODcsImp0aSI6IjU2ZWI1YmRkZjBjMDkwNWNkZWNmMWNkYzBmNTViYjY0In0.r7M2SMKECiSdMdSNcuqO8JIQcV9JeE4YIwe56pIW_iA"


def addr_to_svy(addr):
    """
    converts an andress to an svy21 coord
    """
    domain = "https://developers.onemap.sg/commonapi/search?searchVal="
    options = "&returnGeom=Y&getAddrDetails=N"
    r = requests.get(domain + addr + options).json()['results'][0]
    return (float(r['X']), float(r['Y']))


def svy_to_wgs(x, y):
    """
    Converts an svy21 coord to wgs48 coord
    """
    url = 'https://developers.onemap.sg/commonapi/convert/3414to4326?'
    params = 'X=' + str(x) + '&Y=' + str(y)
    r = requests.get(url + params).json()
    return str(r['latitude']) + "," + str(r['longitude'])


def find_nearest(ax, ay):
    """
    Given (ax, ay) coord, find (bx, by) of closest carpark
    """
    loturl = 'https://api.data.gov.sg/v1/transport/carpark-availability'
    with open('carpark_data.json') as f:
        carpark_list = json.load(f)
    biglist = []
    Jlots = requests.get(loturl).json()
    lots = Jlots['items'][0]['carpark_data']
    adict = {}
    for lot in lots:
        adict[lot['carpark_number']] = int(lot['carpark_info'][0]['lots_available'])

    for b in carpark_list:
        xb = float(b['x'])
        yb = float(b['y'])
        carparkb = b['carpark_number']
        try:
            lots_left = adict[carparkb]
            # print(lots_left, carparkb, math.hypot(ax - xb, ay - yb))
            if carparkb in adict.keys() and lots_left > 0:
                biglist.append((math.hypot(ax - xb, ay - yb), carparkb, xb, yb, lots_left))
        except KeyError:
            continue
    r = min(biglist)
    return (r[2], r[3], r[4])


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """
    Handles
    """
    if request.method == 'POST':
        xa, ya = addr_to_svy(request.form['address'])
        start = svy_to_wgs(xa, ya)
        xb, yb, lots = find_nearest(xa, ya)
        end = svy_to_wgs(xb, yb)
    else:
        start = "1.37219780826066,103.901539947637"
        end = "1.37219780826066,103.901539947637"
        lots = "-"
    return render_template('index.html', start=start, end=end, lots=lots)

@app.route('/postmethod', methods=['POST'])
def postmethod():
    """
    Handling AJAX
    """
    data = request.get_json()
    print(data)
    xa = data['location']['lat']
    ya = data['location']['lng']
    start = str(xa) + "," + str(ya)
    print(start)
    xb, yb, lots = find_nearest(xa, ya)
    end = svy_to_wgs(xb, yb)
    print(end)
    # import pdb; pdb.set_trace()
    return render_template('index.html', start=start, end=end, lots=lots)
    # return jsonify(data)
