from django.db import models
from users.models import User


class Match(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE,related_name="owner")
    match = models.OneToOneField(User, on_delete=models.CASCADE,related_name="match")
    created_at = models.DateTimeField(auto_now_add=True)
