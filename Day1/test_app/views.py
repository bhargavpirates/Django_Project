from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hello_world_view(request):
    servertime=datetime.datetime.now()
    #s="servertime :: {servertime}"
    print_val="current Date and Time of server :: " +  str(servertime)
    return HttpResponse(f"<h1> This is Response from Django Application <h1><h2> {print_val} <h2>")

# Create your views here.
def first_view(request):
    return HttpResponse(f"<h1> This is Response from Django Application from frist view method <h1>")

# Create your views here.
def second_view(request):
    return HttpResponse(f"<h1> This is Response from Django Application from second view method<h1>")