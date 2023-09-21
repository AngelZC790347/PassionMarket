from django.db import models
from users.models import User


class Match(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    match = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)