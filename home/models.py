from django.db import models

# Create your models here.
class Homes(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    depname = models.CharField(max_length=50)
    gpa = models.CharField(max_length=4)