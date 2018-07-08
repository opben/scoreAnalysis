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
        
        return render(request,"scoreCharts.html",{'res':total, 'choice':cho})    

    if request.method == "POST":
        pass

