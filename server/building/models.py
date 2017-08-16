from django.db import models


class House(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    house = models.ForeignKey(House, related_name='rooms')

    def __str__(self):
        return self.name + '_from_' + str(self.house)
