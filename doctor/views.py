from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from results.models import PatientProfile, ResultsModel
from django.http import HttpResponseRedirect, HttpResponse
from pymongo.errors import DuplicateKeyError, BulkWriteError
from results.forms import AddResultForm
from accounts.models import UserProfile
from django.contrib.auth.models import User
from predict.views import see_prediction


@login_required
@user_passes_test(lambda u: UserProfile.objects.get(user_id=User.objects.get(id=u.id).id).staff == 'Doctor')
def doctor_home(request):
    patient = PatientProfile.objects.all()
    results = ResultsModel.objects.all()

    if request.method == 'POST':
        form = AddResultForm(request.POST)
        result_id = request.POST.get('result_input', None)

        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('')

            except BulkWriteError:
                return render(request, 'doctor/doctor_home.html', {'patient': patient, 'results': results, 'form_status': 'none',
                                                                 'tab_1_active': '', 'tab_2_active': 'active'})

            except DuplicateKeyError:
                return render(request, 'doctor/doctor_home.html', {'patient': patient, 'results': results, 'form_status': 'none',
                                                                 'tab_1_active': '', 'tab_2_active': 'active'})

        if result_id is not None:
            try:
                result = ResultsModel.objects.get(result_id=result_id)
                return render(request, 'doctor/doctor_home.html', {'result': result, 'result_id': result_id, 'patient': patient, 'results': results,
                                                                   'form_status': 'block',
                                                                   'tab_1_active': '', 'tab_2_active': 'active'})

            except results.DoesNotExist:
                return HttpResponse("no such result")

        form = AddResultForm(request.GET)

        args = {'form': form, 'patient': patient, 'results': results, 'form_status': 'none',
                'tab_1_active': '', 'tab_2_active': 'active'}

        return render(request, 'doctor/doctor_home.html', args)

    else:
        form = AddResultForm()
        args = {'form': form, 'patient': patient, 'results': results, 'form_status': 'none',
                'tab_1_active': 'active', 'tab_2_active': ''}

        return render(request, 'doctor/doctor_home.html', args)


@login_required
@user_passes_test(lambda u: UserProfile.objects.get(user_id=User.objects.get(id=u.id).id).staff == 'Doctor')
def see_prediction2(request):
    print("adfsadfasdfasdfdfasfd")
    return see_prediction(request)

