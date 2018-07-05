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
        return render(request,"scoreCharts.html")    
    if request.method == "POST":
        pass

