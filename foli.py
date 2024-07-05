import pandas as pd
import numpy as np
import folium
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap
from folium.plugins import FastMarkerCluster

def map():
    locations=pd.read_csv('zomato_locations.csv')
    geolocator=Nominatim(user_agent='app')
    lat=[]
    lon=[]
    for location in locations['Name']:
        location=geolocator.geocode(location)
        if location is None:
            lat.append(np.nan)
            lon.append(np.nan)
        else:
            lat.append(location.latitude)
            lon.append(location.longitude)

    locations['lat']=lat
    locations['lon']=lon

    basemap=generatebasemap()
    # HeatMap(locations[["lat","lon","count"]],zoom=20).add_to(basemap)
    FastMarkerCluster(locations[["lat","lon","count"]],zoom=20).add_to(basemap)
    HeatMap(locations[['lat','lon','avg_rating']]).add_to(basemap)
    map_html = basemap._repr_html_()
    return map_html

def generatebasemap(default_location=[12.97,77.59],default_zoom_start=12):  # you can give any random value from our dataframe as default location
        basemap=folium.Map(location=default_location,zoom_start=default_zoom_start)
        return basemap

