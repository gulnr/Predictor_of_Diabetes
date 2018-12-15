from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password_confirm = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    staff = forms.CharField(label='Staff Type', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Doctor'}), required=True)
    birthdate = forms.CharField(label='Birthdate', widget=forms.DateInput(format='%d.%m.%Y', attrs={'class':'form-control', 'placeholder':'Doctor'}))
    phonenumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'+90 '}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'password_confirm',
            'staff',
            'email',
            'birthdate',
            'phonenumber'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password = self.cleaned_data['password']
        user.password_confirm = self.cleaned_data['password_confirm']
        user.staff = self.cleaned_data['staff']
        user.email = self.cleaned_data['email']
        user.birthdate = self.cleaned_data['birthdate']
        user.phonenumber = self.cleaned_data['phonenumber']

        u = User(username=user.username, first_name=user.first_name, last_name=user.last_name,
                 password=make_password(user.password))
        up = UserProfile(staff=user.staff, birthdate=user.birthdate, phonenumber=user.phonenumber)

        if commit and(user.password != user.password_confirm):
            u.save()
            up.save()

        return u, up


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
        exclude = []

class AdditionalInfoForm(forms.Form):
    phonenumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    address = forms.CharField(label='Address', widget=forms.TextInput, required=True)

    class Meta:
        model = UserProfile
        fields = ('phonenumber',
                  'address',
        )
        exclude = []

    def save(self, commit=True):
        user = super(AdditionalInfoForm, self).save(commit=False)
        user.phonenumber = self.cleaned_data['phonenumber']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()

        return user