from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .shorten_url.shorten import shorten_url
from .models import ModelURL
# from .serializers import URLSerializer
def hello(request):
    return render(request, 'home.html')
    # return JsonResponse({'MSG':"Hello"})

# Get Shortner URL
@api_view(['POST'])
def get_short_url(request):
    if request.method == 'POST':
        print(request.POST)
        print("get_shortner URL")
        get_tiny_url = shorten_url('www.google.com')
        print(get_tiny_url)
        
        return JsonResponse({"short_url":get_tiny_url})
    