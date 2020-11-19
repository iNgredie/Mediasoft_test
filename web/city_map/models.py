from django.db import models


class City(models.Model):
    title = models.CharField('название', max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'


class Street(models.Model):
    title = models.CharField('название', max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return f'{self.title}'


class Shop(models.Model):
    title = models.CharField('название', max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.IntegerField('дом')
    opening_time = models.TimeField('время открытия')
    closing_time = models.TimeField('время закрытия')
    open = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.title}, {self.city}, {self.street}'