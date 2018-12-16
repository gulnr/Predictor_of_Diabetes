from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff = models.CharField(max_length=30, default='Doctor')
    phonenumber = models.CharField(max_length=14, default='90 ')
    birthdate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)