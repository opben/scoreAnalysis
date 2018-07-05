from django.db import models

class score(models.Model):
    stuId = models.CharField(max_length=50)
    choice = models.IntegerField()
    blank = models.IntegerField()
    q17 = models.IntegerField()
    q18 = models.IntegerField()
    q19 = models.IntegerField()
    q20 = models.IntegerField()
    q21 = models.IntegerField()
    q22 = models.IntegerField()
    q23 = models.IntegerField()
    q24 = models.IntegerField()
    q25 = models.IntegerField()
    q26 = models.IntegerField()
    q27 = models.IntegerField()
    total = models.IntegerField()

class statistic(models.Model):
    queId = models.CharField(max_length=50)
    maxS = models.IntegerField()
    minS = models.IntegerField()
    avg = models.FloatField()
    bzc = models.FloatField()   # 标准差
    