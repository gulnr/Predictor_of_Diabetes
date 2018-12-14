from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm, AdditionalInfoForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'account/login.html')


@login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        additional = AdditionalInfoForm(request.POST)

        if form.is_valid() and additional.is_valid():
            print(form)
            print(additional)
            form.save()
            additional.save()
            return HttpResponseRedirect('/account')
    else:
        form = RegistrationForm()
        additional = AdditionalInfoForm()
        args = {'form': form, 'additional': additional}
        return render(request, 'accounts/register_form.html', args)


@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)



