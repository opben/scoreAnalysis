from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name = 'scoreQuery'
urlpatterns=[
    re_path(r'', views.scoreQuery, name='scoreQuery'),
]