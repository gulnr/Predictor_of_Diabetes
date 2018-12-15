from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    staff = forms.CharField(label='Staff Type', widget=forms.TextInput, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'staff',
            'email',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.staff = self.cleaned_data['staff']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


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