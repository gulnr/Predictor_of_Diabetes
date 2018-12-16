from django.urls import re_path
from doctor import views

app_name = 'doctor'

urlpatterns =[
    re_path(r'^doctor_home/$', views.doctor_home, name='doctor_home'),
]