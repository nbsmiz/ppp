import googlemaps
from datetime import datetime as dt

file = open('api_key.txt', 'r')
key = file.read()

gmaps = googlemaps.Client(key)

# geo = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

print(geo)