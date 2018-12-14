from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, blank=False, default='')
    surname = models.CharField(max_length=20, blank=False, default='')
    is_staff = models.BooleanField(default=True)
    phonenumber = models.CharField(max_length=12, default='+90 ')
    address = models.CharField(max_length=200, default='', blank=False)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)