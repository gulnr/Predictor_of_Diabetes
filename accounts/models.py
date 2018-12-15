from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, default='')
    surname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=30, default='')
    staff = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=14, default='+90 ')
    address = models.CharField(max_length=200, default='', blank=False)
    description = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)