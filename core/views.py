from django.shortcuts import render
from model import model
from django.http import JsonResponse
from foli import map
import os,json,pandas as pd

df=pd.read_csv('data_proc.csv')
cur_lat = 0
cur_lon = 0
# Create your views here.
def home(request): 
    initia()      
    return render(request,'home.html')

def recommendation(request):
    with open('data.json') as f:
        data = json.load(f)
    with open('loc.json') as f:
        loc = json.load(f)
    cur_loc=loc['cur_loc']
    keys = list(data.keys())
    keys=keys[1:]
    data = {key: data[key] for key in keys}
    context={"data":data,"cur_loc":cur_loc}
    return render(request,'recommendation.html',context)

def hotspot(request):
    map_html = map()
    context = {"map_html": map_html}
    return render(request,'hotspot.html',context)

def json_data(request):
    with open('data.json') as f:
        data = json.load(f)
    with open('loc.json') as f:
        loc = json.load(f)
    keys = list(data.keys())
    keys=keys[1]
    cur_lat = loc['cur_lat']
    cur_lon = loc['cur_lon']
    des_lat=(data[keys][0])
    des_lon=(data[keys][1])
    lat_lon={"cur_lat":cur_lat,"cur_lon":cur_lon,"des_lat":des_lat,"des_lon":des_lon}
    return JsonResponse(lat_lon)

def initia():
    data=model()

    # write data to a file 
    with open('data.json', 'w') as f:
        json.dump(data[0], f)
    loc=(data[1])
    cur_loc=loc['Station Names']
    cur_lat = loc['Latitude']
    cur_lon = loc['Longitude']
    loc_data={"cur_loc":cur_loc,"cur_lat":cur_lat,"cur_lon":cur_lon}
    with open('loc.json','w') as f:
        json.dump(loc_data,f)

