from django.db import models


class City(models.Model):
    title = models.CharField('название', max_length=255, unique=True)

    def __str__(self):
        return '%s' % self.title


class Street(models.Model):
    title = models.CharField('название', max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return '%s' % self.title


class Shop(models.Model):
    title = models.CharField('название', max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.IntegerField('дом')
    opening_time = models.TimeField('время открытия')
    closing_time = models.TimeField('время закрытия')
    open = models.BooleanField(default=1, null=True)

    def get_status(self, localtime):
        closing_shops = Shop.objects.filter(opening_time__lte=localtime).exclude(closing_time__gte=localtime)
        opening_shops = Shop.objects.filter(opening_time__gte=localtime).exclude(closing_time__lte=localtime)

        for shop in closing_shops:
            shop.open = 0
            shop.save()

        for shop in opening_shops:
            shop.open = 1
            shop.save()

    def __str__(self):
        return f'{self.title}, {self.city.title}, {self.street.title}'

