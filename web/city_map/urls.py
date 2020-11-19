from django.conf.urls import url
from rest_framework import routers

from .views import CityViewSet, ShopViewSet, StreetsInTheCityList

urlpatterns = [
    url('city/(?P<pk>[^/.]+)/street', StreetsInTheCityList.as_view()),
]


router = routers.SimpleRouter()
router.register(r'city', CityViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns += router.urls
