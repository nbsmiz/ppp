import requests
import geocoder

g = geocoder.osm("45039")
print(g.latlng)