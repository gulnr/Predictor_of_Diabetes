from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def doctor_home(request):
    return render(request, 'staff/doctor_home.html')