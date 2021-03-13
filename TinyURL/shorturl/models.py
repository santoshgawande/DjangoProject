from django.db import models

# Create your models here.
class ModelURL(models.Model):
    long_url = models.CharField(max_length=40)
    short_url = models.CharField(max_length=7)



