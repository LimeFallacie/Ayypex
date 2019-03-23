
#this code snippet queries HDB carpark information
import urllib
url = 'https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&limit=5&q=title:jones'
fileobj = urllib.urlopen(url)

print fileobj.read()

