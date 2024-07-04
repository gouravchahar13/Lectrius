from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        loc=request.POST['location']
        # feed to model
        result=get_distance(loc)
        
    return render(request,'home.html')