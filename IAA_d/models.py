from django.db import models
class buystockdata(models.Model):
    username=models.CharField(max_length=20)
    ticker=models.CharField(max_length=4)
    quantity=models.IntegerField()

class buysdata(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=40)
    ticker=models.CharField(max_length=4)
    quantity=models.IntegerField()

class activitysdata(models.Model):
    username=models.CharField(max_length=20)
    desc=models.CharField(max_length=100)
    name=models.CharField(max_length=40)
    ticker=models.CharField(max_length=10)
    quantity=models.IntegerField()
    dtime=models.DateTimeField()

