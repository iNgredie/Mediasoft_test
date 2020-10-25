import time

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer, StreetsInTheCitySerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    localtime = time.strftime("%H:%M:%S")
    Shop.get_status(queryset, localtime)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['street', 'city', 'open']


class StreetsInTheCityList(generics.ListAPIView):
    serializer_class = StreetsInTheCitySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Street.objects.filter(city_id=pk)
