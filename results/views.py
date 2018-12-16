from django.shortcuts import render
from results.forms import AddResultForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from pymongo.errors import DuplicateKeyError


@login_required
def labasst_home(request):
    if request.method == 'POST':
        form = AddResultForm(request.POST)

        if form.is_valid():
            print(form)
            try:
                form.save()
                return HttpResponseRedirect('')

            except DuplicateKeyError:
                return render(request, 'staff/labasst_home.html')

        args = {'form': form}
        return render(request, 'staff/labasst_home.html', args)

    else:
        form = AddResultForm()
        args = {'form': form}
        return render(request, 'staff/labasst_home.html', args)
