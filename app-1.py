from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
import folium as f
import geocoder as geo

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index2.html')


@app.route('/map', methods=['POST', 'GET'])
def map():
    g = geo.osm('06039 USA')  # geocode user input
    start_coords = g.latlng  # set view map center to latitude and longitude 
    m = f.Map(location = [0,0], zoom_start=12)  # location required in order to modify with user input
    m.location = start_coords  # change map view location to user input
    return m._repr_html_()


@app.route('/map2')
def map2():
    return render_template('view_map.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
