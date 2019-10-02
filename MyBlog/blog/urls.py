from django.urls import path
from . import views

urlpatterns = [
    #space causes error : path did not found
    path('', views.home, name='blog-home'),
    
    path('about/', views.about, name='blog-about'), 

]
#import pdb; pdb.set_trace()