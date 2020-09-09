from django.db import models
from django.contrib.auth.models import User


class Universe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hero_pics')
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
