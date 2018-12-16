from django.shortcuts import render
from results.forms import AddResultForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from pymongo.errors import DuplicateKeyError, BulkWriteError
from results.models import *
from accounts.models import UserProfile

@login_required
@user_passes_test(lambda u: UserProfile.object(staff='Laboratory Assistant') in u.groups.all())
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
                return render(request, 'results/labasst_home.html')

            except DuplicateKeyError:
                return render(request, 'results/labasst_home.html')

        if result_id is not None:
            try:
                result = ResultsModel.objects.filter(result_id=result_id).first()
                update_form = AddResultForm(instance=result)
                result2 = ResultsModel.objects.filter(result_id=result_id).delete()

                return render(request, 'results/labasst_home.html', {'update_form': update_form, 'result_id':result_id})

            except ResultsModel.DoesNotExist:
                return HttpResponse("no such result")

        if result_id2rm is not None:
            try:
                result = ResultsModel.objects.filter(result_id=result_id2rm).delete()

                return render(request, 'results/labasst_home.html',
                              { 'result_id2rm': (result_id2rm + ' removed')})

            except ResultsModel.DoesNotExist:
                return HttpResponse("no such result")

        form = AddResultForm(request.GET)

        args = {'form': form}
        return render(request, 'results/labasst_home.html', args)

    else:
        form = AddResultForm()
        args = {'form': form}
        return render(request, 'results/labasst_home.html', args)

