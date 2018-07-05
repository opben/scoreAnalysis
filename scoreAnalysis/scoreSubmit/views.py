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
from .models import score,statistic

def getSum(x, y):
    return x + y

def getAvg(list):
    sum = reduce(getSum, list)
    return float(sum/len(list))

def scoreSubmit(request):                  
    if request.method == "GET":
        return render(request,"index.html")    
    if request.method == "POST":
        i = request.POST
        if "submit" in i:
            file = request.FILES['excel'].read()
            wb = xlrd.open_workbook(filename=None, file_contents=file)
            table = wb.sheets()[0]  # 获取一个工作表sheet，索引从0开始
            rows = table.nrows
            cols = table.ncols
            for row in range(3,rows):
                item = table.row_values(row)
                score.objects.create(stuId=item[0], choice=item[1],blank=item[2], q17=item[3],
                    q18=item[4], q19=item[5], q20=item[6], q21=item[7], q22=item[8], q23=item[9],
                    q24=item[10], q25=item[11], q26=item[12], q27=item[13], total=item[14])

            for col in range(1,cols):
                item = table.col_values(col)
                if col == 1:
                    queId = 'choice'
                elif col == 2:
                    queId = 'blank'
                elif col == cols - 1:
                    queId = 'total'
                else:
                    queId = 'q' + str(col + 14)
                maxS = max(item[3:])
                minS = min(item[3:])
                avg = getAvg(item[3:])
                std = float(np.std(item[3:]))
                statistic.objects.create(queId=queId, maxS=maxS, minS=minS, avg=avg, bzc=std)

        return render(request,"index.html",{'res':1})

