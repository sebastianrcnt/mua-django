from django.db import models

# Create your models here.
class Recruit(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=30)