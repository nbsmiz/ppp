from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
import folium as f
import geocoder as geo
from lib.map import add_loans_to_map

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


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


@app.route('/view_map', methods=['POST', 'GET'])
def map2():
    return render_template('view_map.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/choro')
def choro():
    return render_template('map_choro_test.html')


@app.route('/sum_by_state')
def sum_by_state():
    return render_template('loan_sum_by_state.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
