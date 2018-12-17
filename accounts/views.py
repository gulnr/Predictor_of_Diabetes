from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm, AdditionalInfoForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from pymongo.errors import DuplicateKeyError, BulkWriteError
from .models import UserProfile
from django.contrib.auth.models import User

def home(request):
    return render(request, 'accounts/login.html')


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
    user = UserProfile.objects.get(user_id=request.user.id)
    print(user)
    args = {'user': user}
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


@login_required
def account(request):
    return render(request, 'accounts/account.html')


@login_required
def see_employees(request):
    staff = UserProfile.objects.filter(staff="Doctor")
    staff2 = UserProfile.objects.filter(staff="Laboratory Assistant")

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST.get('username_input', None)
        username2rm = request.POST.get('username_input_remove', None)

        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('')

            except BulkWriteError:
                return render(request, 'staff/manager_v2.html', {'staff': staff, 'staff2': staff2, 'form_status': 'none',
                                                                 'tab_1_active': '', 'tab_2_active':'active', 'tab_3_active': '',
                                                                 'tab_4_active': ''})

            except DuplicateKeyError:
                return render(request, 'staff/manager_v2.html', {'staff': staff, 'staff2': staff2, 'form_status':'none',
                                                                 'tab_1_active': '', 'tab_2_active': 'active',
                                                                 'tab_3_active': '',
                                                                 'tab_4_active': ''
                                                                 })

        if username is not None:
            try:
                user = User.objects.filter(username=username).first()
                update_form = RegistrationForm(instance=user)
                return render(request, 'staff/manager_v2.html', {'update_form': update_form, 'username':username, 'staff': staff, 'staff2': staff2,
                                                                 'form_status':'block',
                                                                 'tab_1_active': '', 'tab_2_active': '',
                                                                 'tab_3_active': 'active',
                                                                 'tab_4_active': ''
                                                                 })

            except User.DoesNotExist:
                return HttpResponse("no such user")

        if username2rm is not None:
            try:
                user = User.objects.filter(username=username2rm).delete()

                return render(request, 'staff/manager_v2.html',
                              { 'username2rm': (username2rm + ' removed'), 'staff': staff, 'staff2': staff2, 'form_status':'none',
                                'tab_1_active': '', 'tab_2_active': '', 'tab_3_active': '',
                                'tab_4_active': 'active'
                                })

            except User.DoesNotExist:
                return HttpResponse("no such user")

        form = RegistrationForm(request.GET)

        args = {'form': form, 'staff': staff, 'staff2': staff2, 'form_status':'none',
                'tab_1_active': 'active', 'tab_2_active': '', 'tab_3_active': '',
                'tab_4_active': ''
                }
        return render(request, 'staff/manager_v2.html', args)

    else:
        form = RegistrationForm()
        args = {'form': form, 'staff': staff, 'staff2': staff2, 'form_status':'none',
                'tab_1_active': 'active', 'tab_2_active': '', 'tab_3_active': '',
                'tab_4_active': ''
                }
        return render(request, 'staff/manager_v2.html', args)

