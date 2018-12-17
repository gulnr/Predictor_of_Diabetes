from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from results.models import PatientProfile, ResultsModel


# Create your views here.

@login_required
def doctor_home(request):
    patient = PatientProfile.objects.all()
    patient2 = ResultsModel.objects.all()

    args = {'patient': patient, 'patient2': patient2}

    return render(request, 'doctor/doctor_home.html', args)
