import math
import requests

ONEMAP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI1MTksInVzZXJfaWQiOjI1MTksImVtYWlsIjoiYm9rd29vbi5jQGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1MzM0MTc4NywiZXhwIjoxNTUzNzczNzg3LCJuYmYiOjE1NTMzNDE3ODcsImp0aSI6IjU2ZWI1YmRkZjBjMDkwNWNkZWNmMWNkYzBmNTViYjY0In0.r7M2SMKECiSdMdSNcuqO8JIQcV9JeE4YIwe56pIW_iA"

def retrieve_carpark_list():
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&limit=5'
    Jlist = requests.get(url).json()

def user_location():
    postal_code = input()
    domain = "https://developers.onemap.sg/commonapi/search?searchVal="
    options = "&returnGeom=Y&getAddrDetails=N"
    #print(requests.get(domain + postal_code + options).json())
    r = requests.get(domain + postal_code + options).json()['results'][0]
    return (r['X'], r['Y'])

#def find_nearest():

def route(start_lat, start_long, end_lat, end_long): #function not done
    domain = 'https://developers.onemap.sg/privateapi/routingsvc/route?start='
    start = '1.319728,103.8421'
    '&end='
    end = '1.319728905,103.8421581'
    '&routeType=drive&token=' + ONEMAP_TOKEN



def check_lots():
    loturl = 'https://api.data.gov.sg/v1/transport/carpark-availability'
    requests.get(loturl).json()


def convert_svy_to_wgs(X, Y): #for inputting params for routing
    url = 'https://developers.onemap.sg/commonapi/convert/3414to4326?'
    params = 'X=' + str(X) + '&Y=' + str(Y)

    print(requests.get(url + params).json())

def main():
    geom = user_location()
    #print(geom) #prints user_location X&Y
    #convert_svy_to_wgs(geom[0], geom[1]) #test conversion function
    #find_nearest(user_location())
    check_lots()

main()

