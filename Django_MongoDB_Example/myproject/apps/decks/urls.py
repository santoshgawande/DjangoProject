from rest_framework import routers
from .views import DeckViewSet
router = routers.SimpleRouter()
router.register(r'', DeckViewSet)
urlpatterns = router.urls