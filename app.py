from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
import folium as f
import geocoder as geo
from lib.map import add_loans_to_map

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index2.html')


@app.route('/map', methods=['POST', 'GET'])
def map():
    if (request.method == 'POST') and request.form.get('zipCode') != '':
        zipCode = request.form.get('zipCode')
    else:
        zipCode = '06071'
    g = geo.osm(zipCode + ' USA')  # geocode user input
    start_coords = g.latlng  # set view map center to latitude and longitude 
    m = f.Map(location = [0,0], zoom_start=12)  # location required in order to modify with user input
    m.location = start_coords  # change map view location to user input
    add_loans_to_map(m)
    return m._repr_html_()


@app.route('/map2', methods=['POST', 'GET'])
def map2():
    if (request.method == 'POST') and request.form.get('zipCode') != '':
        zipCode = request.form.get('zipCode')
        return render_template('view_map.html', zipCode=zipCode)
    else:
        return render_template('view_map.html', zipCode='06071')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
