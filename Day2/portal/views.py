from django.shortcuts import render
import datetime


# Create your views here.
def news_app(request):
    msg="Welocome to NEW Publish Portal"
    date=datetime.datetime.now()
    response= render(request,'portal/news.html',{'msg':msg,'date':date})
    return response

def movie_news_view(request):
    news1="NTR Remunartion 50 crores!!!"
    news2="PK signed 5 movies at a Time"
    news3="Chirus new  film begain after corona"
    news4="Ram going to act in Tamil movie"
    my_dict={"news1":news1,"news2":news2,"news3":news3,"news4":news4}
    return render(request,'portal/mnews.html',my_dict)
