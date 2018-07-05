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
from scoreSubmit.models import score

def scoreQuery(request):                  
    if request.method == "GET":
        return render(request, "scoreQuery.html")    
    if request.method == "POST":
        i = request.POST
        res = 0
        if "submit_stu" in i:
            stuId = i['stuId']
            res1 = score.objects.filter(stuId=stuId)
            return render(request, "scoreQuery.html", {'res1':res1})

        if "submit_que" in i:
            inp = i['que'].split(',')
            stuId = inp[0]
            queId = inp[1]
            res = score.objects.values(queId).filter(stuId=stuId)[0]
            qScore = res[queId]
            return render(request, "scoreQuery.html", {'res':res, 'queId':queId, 
                                                    'stuId':stuId, 'qScore':qScore})