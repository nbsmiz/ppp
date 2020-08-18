from flask import Flask, render_template, request, redirect, session
from flask_googlemaps import GoogleMaps
import folium

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

API_KEY = "AIzaSyDH1FdEzMrPOj3V1bxIwA5hdQmhP4brCaU"

@app.route('/map')
def map():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(port=33507, debug=True)
