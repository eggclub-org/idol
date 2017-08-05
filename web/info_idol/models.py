from django.db import models

# Create your models here.
class InfoIdol(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField()
    height = models.PositiveIntegerField()
    v1 = models.PositiveIntegerField()
    v2 = models.PositiveIntegerField()
    v3 = models.PositiveIntegerField()
    list_film = models.TextField()