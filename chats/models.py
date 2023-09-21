from django.db import models
from matches.models import Match


class Chat(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE, verbose_name="the related Match")
    file_Chat = models.FilePathField()
