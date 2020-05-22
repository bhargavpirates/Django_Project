from django.conf.urls import url
from test_app import views


urlpatterns = [
    url(r'^hello/', views.hello_world_view),
    url(r'^firstview/', views.first_view),
    url(r'^secondview/', views.second_view),
]