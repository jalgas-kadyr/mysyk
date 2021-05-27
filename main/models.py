from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    age = models.IntegerField()
    legs = models.IntegerField()
    price = models.IntegerField()
    image = models.CharField(max_length=20)

    def __str__(self):
        return self.name
