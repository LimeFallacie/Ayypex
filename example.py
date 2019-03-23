#this code snippet queries HDB carpark information
import requests

ONEMAP_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI1MTksInVzZXJfaWQiOjI1MTksImVtYWlsIjoiYm9rd29vbi5jQGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1MzM0MTc4NywiZXhwIjoxNTUzNzczNzg3LCJuYmYiOjE1NTMzNDE3ODcsImp0aSI6IjU2ZWI1YmRkZjBjMDkwNWNkZWNmMWNkYzBmNTViYjY0In0.r7M2SMKECiSdMdSNcuqO8JIQcV9JeE4YIwe56pIW_iA"

def retrieve_carpark_list():
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&limit=5'
    Jlist = requests.get(url).json()

def user_location():
    postal_code = input()


#def find_nearest():




def convert_svy_to_wgs(): #for inputting params for routing
    url = 'https://developers.onemap.sg/commonapi/convert/3414to4326?'
    params = 'X=28983.788791079794&Y=33554.5098132845'

    print(requests.get(url + params).json())

def main():
    user_location()
    convert_svy_to_wgs()
    #find_nearest(user_location())


main()

