from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
import folium
import geocoder as geo

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/map', methods=['POST'])
def map():
    g = geo.osm('45039 USA')
    start_coords = g.latlng
    # folium_map = folium.Map(location= start_coords, zoom_start=12)
    folium_map = folium.Map(location = [0,0], zoom_start=12)  # location required in order to modify with user input
    folium_map.location = start_coords  # change map view location to user input
    return folium_map._repr_html_()


@app.route('/map2')
def map2():
    return render_template('map-var.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
