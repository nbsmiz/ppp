from flask import Flask, render_template, request, redirect, session
from flask_googlemaps import GoogleMaps

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():



if __name__ == '__main__':
  app.run(port=33507)
