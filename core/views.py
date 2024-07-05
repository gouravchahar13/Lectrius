from django.shortcuts import render
from model import model
from django.http import JsonResponse
from foli import map

# Create your views here.
def home(request):       
    return render(request,'home.html')

def recommendation(request):
    data=model()
    cur_loc = data[1]['Station Names']
    data=data[0]
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
    data=model()
    cur_lat = data[1]['Latitude']
    cur_lon = data[1]['Longitude']
    data=data[0]
    keys = list(data.keys())
    keys=keys[1]
    des_lat=(data[keys][0])
    des_lon=(data[keys][1])
    lat_lon={"cur_lat":cur_lat,"cur_lon":cur_lon,"des_lat":des_lat,"des_lon":des_lon}
    return JsonResponse(lat_lon)
