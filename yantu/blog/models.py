from django.db import models

# Create your models here.
class Tiltle(models.Model):
    tiltlename = models.CharField(max_length=100)
    tiltlecontent = models.CharField(max_length=500)
