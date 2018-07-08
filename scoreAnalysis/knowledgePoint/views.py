#coding=utf-8
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from math import log
import xlrd
import pymysql  #py3, instead of MySQLdb
import string,io #py3, instead of StringIO
import numpy as np
import pandas as pd
import json
import random
import os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import operator
from .models import zsd,zsdTh

def knowledgePointF(request):
    if request.method == "GET":
        return render(request,"knowledgePoint.html")
    if request.method == "POST":
        i = request.POST

        if "submit" in i:
            kpName = i[u'kpName']
            queIds = i['queId'].split(',')

            if(zsd.objects.filter(kpName=kpName).exists()==False): 
            # 知识点表中不存在这个知识点
                zsd.objects.create(kpName=kpName)   # 插入知识点
                kpId = zsd.objects.all().first().id + zsd.objects.all().count() - 1 # 获取第一个知识点的id
                for j in queIds:
                    zsdTh.objects.create(kpId=kpId,queId=int(j))  # 插入知识点-题目表
            return render(request, "knowledgePoint.html", {'res1':kpId})

        elif "query_kno" in i:  # 按题号
            queId = i['queId']
            kpId = zsdTh.objects.filter(queId=queId)[0].kpId
            kpName = zsd.objects.filter(id=kpId)[0].kpName
            return render(request, "knowledgePoint.html", {'res2':1, 'queId':queId, 'kpName':kpName})

        elif "query_queId" in i:  # 按知识点
            kpName = i[u'knoId']
            kpId = zsd.objects.filter(kpName=kpName)[0].id
            queId = zsdTh.objects.filter(kpId=kpId)
            res = []
            for j in queId:
                res.append(j.id)
            return render(request, "knowledgePoint.html", {'res2':1, 'queId':res, 'kpName':kpName})
