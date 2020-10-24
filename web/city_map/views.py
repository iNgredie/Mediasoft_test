from rest_framework.viewsets import ModelViewSet

from .models import City, Street
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = ShopSerializer
