from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import redis
from .scrapping.get_data import import_data

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)

# @api_view(['GET', 'POST'])
# def manage_items(request, *args, **kwargs):
#     if request.method == 'GET':
#         items = {}
#         count = 0
#         for key in redis_instance.keys("*"):
#             items[key.decode("utf-8")] = redis_instance.get(key)
#             count += 1
#         response = {
#             'count': count,
#             'msg': f"Found {count} items.",
#             'items': items
#         }
#         return Response(response, status=200)

#     elif request.method == 'POST':
#         item = json.loads(request.body)
#         key = list(item.keys())[0]
#         value = item[key]
#         redis_instance.set(key, value)
#         response = {
#             'msg': f"{key} successfully set to {value}"
#         }
#         return Response(response, 201)


@cache_page(CACHE_TTL)
def home(request):
    import_data()

    # print("Hi :", redis_instance.keys("*"))
    # items = []
    # for key in redis_instance.keys("*"):
    #     items[key.decode("utf-8")] = redis_instance.get(key)
    #     count += 1
    #     response = {
    #         'count': count,
    #         'msg': f"Found {count} items.",
    #         'items': items
    #     }
    return render(request, 'home.html', {
        'data':"Hi Redis"
    })


@api_view(['GET'])
def view_stock(request):
    equities = Equity.objects.all()
    results = [equity.to_json() for equity in equities]
    print("result :", results)
    return Response(results, status=status.HTTP_201_CREATED)
# # Create your views here.
# def home(request):
#     return render(request, 'home.html')
