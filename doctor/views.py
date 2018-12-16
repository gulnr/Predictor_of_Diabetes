from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def doctor_home(request):
    return render(request, 'doctor/doctor_home.html', locals())