from django.shortcuts import render
from results.forms import AddResultForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from pymongo.errors import DuplicateKeyError, BulkWriteError
from results.models import *
from accounts.models import UserProfile
from django.contrib.auth.models import User

def get_current_username(request):
    print(request.user.username)
    return request.user.username

@login_required
@user_passes_test(lambda u: UserProfile.objects.get(user_id=User.objects.get(id=u.id).id).staff == 'Laboratory Assistant')
def labasst_home(request):
    if request.method == 'POST':
        form = AddResultForm(request.POST)
        result_id = request.POST.get('result_id_input', None)
        result_id2rm = request.POST.get('result_id_input_remove', None)

        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('')

            except BulkWriteError:
                return render(request, 'results/labasst_home.html', {'form_status':'none', 'tab_2_active': 'active',
                                                                     'tab_3_active': '', 'tab_4_active': ''})

            except DuplicateKeyError:
                return render(request, 'results/labasst_home.html', {'form_status':'none', 'tab_2_active': 'active',
                                                                     'tab_3_active': '', 'tab_4_active': ''})

        if result_id is not None:
            try:
                result = ResultsModel.objects.filter(result_id=result_id).first()
                update_form = AddResultForm(instance=result)
                result2 = ResultsModel.objects.filter(result_id=result_id).delete()

                return render(request, 'results/labasst_home.html', {'update_form': update_form, 'result_id':result_id,
                                                                     'form_status': 'block', 'tab_2_active': '',
                                                                     'tab_3_active': 'active', 'tab_4_active': ''})

            except ResultsModel.DoesNotExist:
                return HttpResponse("no such result")

        if result_id2rm is not None:
            try:
                result = ResultsModel.objects.filter(result_id=result_id2rm).delete()

                return render(request, 'results/labasst_home.html',
                              { 'result_id2rm': (result_id2rm + ' removed'), 'form_status':'none', 'tab_2_active': '',
                                'tab_3_active': '', 'tab_4_active': 'active'})

            except ResultsModel.DoesNotExist:
                return HttpResponse("no such result")

        form = AddResultForm(request.GET)

        args = {'form': form, 'form_status':'none', 'tab_2_active': 'active', 'tab_3_active': '',
                'tab_4_active': ''}
        return render(request, 'results/labasst_home.html', args)

    else:
        form = AddResultForm()
        args = {'form': form, 'form_status': 'none', 'tab_2_active': 'active', 'tab_3_active': '',
                'tab_4_active': ''}
        return render(request, 'results/labasst_home.html', args)

