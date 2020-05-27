from django.conf.urls import url
from news_publish_app import views



urlpatterns = [
    url(r'^news/', views.news_app),
]