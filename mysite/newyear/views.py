from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'newyear/files/wishes.html')
    #return HttpResponse("Happy new Year 2020")