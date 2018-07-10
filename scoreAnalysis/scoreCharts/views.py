#coding=utf-8
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from math import log
from functools import reduce
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
from scoreSubmit.models import score,statistic

def scoreCharts(request):                  
    if request.method == "GET":
        # 总分图
        n0_10 = score.objects.filter(total__lte = 10).count()
        n11_20 = score.objects.filter(total__range = (11,20)).count()
        n21_30 = score.objects.filter(total__range = (21,30)).count()
        n31_40 = score.objects.filter(total__range = (31,40)).count()
        n41_50 = score.objects.filter(total__range = (41,50)).count()
        n51_60 = score.objects.filter(total__range = (51,60)).count()
        n61_70 = score.objects.filter(total__range = (61,70)).count()
        n71_80 = score.objects.filter(total__range = (71,80)).count()
        n81_90 = score.objects.filter(total__range = (81,90)).count()
        n91_100 = score.objects.filter(total__range = (91,100)).count()
        total = [n0_10, n11_20, n21_30, n31_40, n41_50, n51_60, n61_70, n71_80, n81_90, n91_100]

        numStu = score.objects.count()  # 总人数
        passed = n61_70 + n71_80 + n81_90 + n91_100
        unpassed = numStu - passed
        pieChart = [{'value':passed, 'name':'及格'},{'value':unpassed, 'name':'不及格'}]

        total2 = score.objects.values('total').order_by("total")  # 总分图，以下类似
        toa = []
        for i in range(len(total2)):
            toa.append([i,total2[i]['total']])

        choice = score.objects.values('choice').order_by("choice")
        cho = []
        for i in range(len(choice)):
            cho.append([i,choice[i]['choice']])

        blank = score.objects.values('blank').order_by("blank")  
        bla = []
        for i in range(len(blank)):
            bla.append([i,blank[i]['blank']])

        # 以下处理17-27题
        a = b = c = d = e = f = g = h = i = g = k = 0
        queId = [a,b,c,d,e,f,g,h,i,g,k]
        res = []

        for i in range(len(queId)):
            ID = 'q' + str(i + 17)
            queId[i] = score.objects.values(ID).order_by(ID)  
            tmp = []
            for j in range(len(queId[i])):
                tmp.append([j,queId[i][j][ID]])
            res.append(tmp)

        return render(request,"scoreCharts.html",{'res':total, 'pie':pieChart, 'total2':toa, 'choice':cho,
                                                'blank':bla, 'q17':res[0],'q18':res[1], 'q19':res[2],
                                                 'q20':res[3], 'q21':res[4], 'q22':res[5],'q23':res[6],
                                                 'q24':res[7], 'q25':res[8], 'q26':res[9], 'q27':res[10]}) 

    if request.method == "POST":
        pass