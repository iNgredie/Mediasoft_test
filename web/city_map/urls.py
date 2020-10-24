from rest_framework import routers

from .views import CityViewSet, StreetViewSet, ShopViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'city', CityViewSet)
router.register(r'street', StreetViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns += router.urls