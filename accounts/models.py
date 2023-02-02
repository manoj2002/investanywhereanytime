from django.db import models

class Profile(models.Model):
    img=models.ImageField()
    username=models.CharField(max_length=30)
