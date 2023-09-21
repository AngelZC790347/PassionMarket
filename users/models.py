from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    birthday = models.DateField()


class UserPassword(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hash = models.CharField(max_length=100)