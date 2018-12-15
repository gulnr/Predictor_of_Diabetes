from django.urls import re_path
from results import views

app_name = 'results'

url_pattern =[
    re_path(r'^labasst_home/$', views.labasst_home, name='labasst_home')


]
