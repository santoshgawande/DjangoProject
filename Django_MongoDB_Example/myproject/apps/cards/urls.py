from rest_framework import routers
from .views import CardViewSet
router = routers.SimpleRouter()
router.register(r'', CardViewSet)
urlpatterns = router.urls