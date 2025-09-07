# Create your models here.

from django.db import models

# Model for user login/registration
class UserAuth(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

# Model for user preferences or yoga session choices
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    goal = models.CharField(max_length=100)
    days = models.CharField(max_length=50)

    def __str__(self):
        return self.name