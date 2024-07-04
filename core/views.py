from django.shortcuts import render
from model import model

# Create your views here.
def home(request):       
    return render(request,'home.html')

def recommendation(request):
    data=model()
    print(data)
    return render(request,'recommendation.html')

def map(request):
    return render(request,'mpp.html')