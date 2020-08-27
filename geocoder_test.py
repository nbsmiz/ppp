import requests
import geocoder

# url = 'https://maps.googleapis.com/maps/api/geocode/json'
# params = {'sensor': 'false', 'address': '1600 Amphitheatre Parkway, Mountain View, CA'}
# r = requests.get(url, params=params)

# g = geocoder.google('1600 Amphitheatre Parkway, Mountain View, CA')
# g = geocoder.google('Mountain View, CA')
g = geocoder.osm("45039")
print(g.latlng)