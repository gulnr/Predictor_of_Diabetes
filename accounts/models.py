from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff = models.CharField(max_length=30, default='Doctor')
    phonenumber = models.CharField(max_length=14, default='90 ')
    birthdate = models.DateField(default=datetime.date.today)
    image = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.user.username

