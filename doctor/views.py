from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your views here.


@login_required
@user_passes_test(lambda u: UserProfile.objects.get(staff="Doctor") in u.groups.all())
def doctor_home(request):
    return render(request, 'doctor/doctor_home.html', locals())