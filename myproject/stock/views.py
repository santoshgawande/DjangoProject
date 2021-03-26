from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
# from cookbook.services import get_recipes

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def home(request):
    return render(request, 'home.html', {
        'data':"Hi Redis"
    })

# # Create your views here.
# def home(request):
#     return render(request, 'home.html')
