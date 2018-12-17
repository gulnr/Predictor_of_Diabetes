from django.urls import re_path
from predict import views

app_name = 'predictions'

urlpatterns =[
    re_path(r'^see_prediction/$', views.see_prediction, name='see_prediction')
]