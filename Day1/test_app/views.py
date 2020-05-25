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

def template_view(request):
    dt=datetime.datetime.now()
    student_name="Bhargav"
    Rollno="AG58855"
    Marks=35
    mydict={'date':dt,'student_name':student_name,"Rollno":Rollno,"Marks":Marks}

    return render(request,'test_app/results.html',context=mydict)

def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg="Hello Guest !!! very Good"
    if(h<12):
        msg=msg+" Morning!!"
    elif(h<16):
        msg=msg+" Afternoon!!"
    elif(h<21):
        msg=msg+" Evening!!"
    else:
        msg=msg+" Night!!"
    
    response= render(request,'test_app/results.html',{'msg':msg,'date':date})
    return response