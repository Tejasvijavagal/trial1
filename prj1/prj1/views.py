
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html' )
def about(request):
    return HttpResponse("this is a about page")