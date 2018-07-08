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

        choice = score.objects.values('choice').order_by("choice")  # 选择题图，以下类似
        cho = []
        for i in range(len(choice)):
            cho.append([i,choice[i]['choice']])

        blank = score.objects.values('blank').order_by("blank")  
        bla = []
        for i in range(len(blank)):
            bla.append([i,blank[i]['blank']])

        q17 = score.objects.values('q17').order_by("q17")  
        d17 = []
        for i in range(len(q17)):
            d17.append([i,q17[i]['q17']])

        q18 = score.objects.values('q18').order_by("q18")  
        d18 = []
        for i in range(len(q18)):
            d18.append([i,q18[i]['q18']])

        q19 = score.objects.values('q19').order_by("q19")  
        d19 = []
        for i in range(len(q19)):
            d19.append([i,q19[i]['q19']])

        q20 = score.objects.values('q20').order_by("q20")  
        d20 = []
        for i in range(len(q20)):
            d20.append([i,q20[i]['q20']])

        q21 = score.objects.values('q21').order_by("q21")  
        d21 = []
        for i in range(len(q21)):
            d21.append([i,q21[i]['q21']])

        q22 = score.objects.values('q22').order_by("q22")  
        d22 = []
        for i in range(len(q22)):
            d22.append([i,q22[i]['q22']])

        q23 = score.objects.values('q23').order_by("q23")  
        d23 = []
        for i in range(len(q23)):
            d23.append([i,q23[i]['q23']])

        q24 = score.objects.values('q24').order_by("q24")  
        d24 = []
        for i in range(len(q24)):
            d24.append([i,q24[i]['q24']])

        q25 = score.objects.values('q25').order_by("q25")  
        d25 = []
        for i in range(len(q25)):
            d25.append([i,q25[i]['q25']])

        q26 = score.objects.values('q26').order_by("q26")  
        d26 = []
        for i in range(len(q26)):
            d26.append([i,q26[i]['q26']])

        q27 = score.objects.values('q27').order_by("q27")  
        d27 = []
        for i in range(len(q27)):
            d27.append([i,q27[i]['q27']])
        
        return render(request,"scoreCharts.html",{'res':total, 'choice':cho, 'blank':bla, 'q17':d17,
                                                'q18':d18, 'q19':d19, 'q20':d20, 'q21':d21, 'q22':d22,
                                                'q23':d23, 'q24':d24, 'q25':d25, 'q26':d26, 'q27':d27})    

    if request.method == "POST":
        pass

