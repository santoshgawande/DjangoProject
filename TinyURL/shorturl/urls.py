from django.urls import path, include
from . import views
urlpatterns =[
        path('', views.hello),
        path('geturl', views.get_short_url)
]