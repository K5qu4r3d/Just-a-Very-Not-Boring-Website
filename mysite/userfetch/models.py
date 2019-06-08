from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=200)
    CCN = models.CharField(max_length=16)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.email
