from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='pics', default='captain_deadpool.jpg')

    def __str__(self):
        return self.user.username + ' profile'