from rest_framework import serializers

from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    streets = serializers.StringRelatedField(many=True)

    class Meta:
        model = City
        fields = ('id', 'title', 'streets')


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field="title", read_only=True)
    street = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'


class StreetsInTheCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ('title', )


