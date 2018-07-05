from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name = 'scoreSubmit'
urlpatterns=[
    re_path(r'', views.scoreSubmit, name='scoreSubmit'),
]