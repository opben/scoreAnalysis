from django.db import models

class zsd(models.Model): # 知识点
    kpName = models.CharField(max_length=255)

class zsdTh(models.Model):   # 知识点-题号
    kpId = models.CharField(max_length=50)
    queId = models.IntegerField()
