from django.db import models

class Users(models.Model):
    name =models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

