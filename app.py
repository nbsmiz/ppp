from flask import Flask, render_template, request, redirect, session
from flask_googlemaps import GoogleMaps

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

API_KEY = "AIzaSyDH1FdEzMrPOj3V1bxIwA5hdQmhP4brCaU"

@app.route('/map')
def map():
    pass

if __name__ == '__main__':
    app.run(port=33507)
