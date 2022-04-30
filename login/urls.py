from unicodedata import name
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
  
  
    #path(r'^panel/del/?P<pk>\d+)/$', views.delete, name="delete"),

]