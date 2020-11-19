import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    streets = serializers.StringRelatedField(many=True)

    class Meta:
        model = City
        fields = (
            'id',
            'title',
            'streets'
        )


class StreetsInTheCitySerializer(ModelSerializer):

    class Meta:
        model = Street
        fields = ('title', )


class ShopSerializer(serializers.ModelSerializer):
    street_title = serializers.StringRelatedField(
        source='street',
        read_only=True
    )
    city_title = serializers.StringRelatedField(
        source='city',
        read_only=True
    )

    open = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = (
            'id',
            'title',
            'street_title',
            'city_title',
            'house',
            'opening_time',
            'closing_time',
            'open'
        )

    def get_open(self, obj: Shop):
        raw_time = datetime.datetime.now().strftime('%H:%M:%S')
        time = list(map(int, raw_time.split(':')))

        now = datetime.time(*time)
        open_field = obj.opening_time < now < obj.closing_time

        if open_field != obj.open:
            obj.open = open_field
            obj.save(update_fields=['open'])
        return open_field



