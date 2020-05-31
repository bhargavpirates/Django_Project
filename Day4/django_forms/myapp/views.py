from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import BlogCommentForm

# Create your views here.
#from .forms import NameForm
""" 
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'testapp/result.html', {'form': form}) """


def showform(request):
    form= BlogCommentForm(request.POST or None)

    if form.is_valid():
        form.save()
        #fname=form.cleaned_data

    context= {'form': form }
        
    return render(request, 'testapp/result.html', context)


def submitform(request):
    servertime=datetime.datetime.now()
    print_val="current Date and Time of server :: " +  str(servertime)
    return HttpResponse(f"<h1> Thanks for submitting a form <h1><h2> {print_val} <h2>")