from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.home, name="home" ),
     url(r'^equities/', views.view_stock, name="equities" ),
   
]