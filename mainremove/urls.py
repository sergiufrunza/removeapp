from django.contrib import admin
from django.urls import path, include, re_path
from mainremove.views import *

urlpatterns = [
   path('', mainView, name='home'),
]