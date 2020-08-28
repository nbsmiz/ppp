import pandas as pd
import pickle
import geocoder as geo
import folium as f
import requests
import re


def add_aClass_loans(latlng, m):
    f.CircleMarker(
        location=latlng,
        radius=7.5,  # use for loan size? scale to size of loan? normalize these?
        popup="$5-10 Million",  # loan value
        color='blue',  # color according to some histogram?
        fill=True,
        fill_color='blue'
    ).add_to(m)


def add_loans_to_map(m):
    a_latlng = pickle.load(open('static/a_latlng.pkd', 'rb'))
    for i in a_latlng.itertuples():
        if i.latlng != None:
            add_aClass_loans(i.latlng, m)