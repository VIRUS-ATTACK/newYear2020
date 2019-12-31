from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request,username = 'your friend'):
    context = {'usernamename':username}
    return render(request,'newyear/files/wishes.html',context)
    #return HttpResponse("Happy new Year 2020")