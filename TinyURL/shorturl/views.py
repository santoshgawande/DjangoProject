from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def hello(request):
    return render(request, 'home.html')
    # return JsonResponse({'MSG':"Hello"})