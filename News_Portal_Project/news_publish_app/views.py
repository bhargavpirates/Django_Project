from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def news_app(request):
    msg="Welocome to NEW Publish Portal"
    date=datetime.datetime.now()
    response= render(request,'news_publish_app/results.html',{'msg':msg,'date':date})
    return response