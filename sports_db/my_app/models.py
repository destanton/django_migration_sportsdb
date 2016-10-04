from django.db import models


class Player(models.Model):
    position = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    at_bat = models.IntegerField()
    runs = models.IntegerField()
    hits = models.IntegerField()
    homeruns = models.IntegerField()
    rbi = models.IntegerField()
