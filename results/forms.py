from django import forms
from .models import PatientProfile, ResultsModel
from datetime import datetime


def calculate_age(bday):
    x = bday.split('/')
    year = x[2]
    month = x[1]
    day = x[0]
    today = datetime.now()
    age = today.year - year
    if month > today.month:
        age = age - 1
    elif month == today.month:
        if day > today.day:
            age = age - 1

    return age


class AddResultForm(forms.ModelForm):

    patient_name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=True)
    patient_surname = forms.CharField(label='Surname', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Last Name'}), required=True)
    patient_birthday = forms.CharField(label='Birthday', widget=forms.DateInput(
        format="%d/%m/%Y", attrs={'class': 'form-control', 'placeholder': 'Day/Month/Year'}), required=True)
    pregnancy = forms.IntegerField(label='# of pregnancies', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '0-17'}), required=True)
    glucose = forms.IntegerField(label='Glucose level', widget=forms.NumberInput(
        attrs={'class': 'form-input', 'placeholder': '0 - 199'}), required=True)
    blood_p = forms.IntegerField(label = 'Blood pressure', widget=forms.NumberInput(
        attrs={'class': 'form-input', 'placeholder': '0-122'}), required=True)
    skin = forms.IntegerField(label='Skin thickness', widget=forms.NumberInput(
        attrs={'class': 'form-input', 'placeholder': '0-99'}), required=True)
    insulin = forms.IntegerField(label='Insulin level', widget=forms.NumberInput(
        attrs={'class': 'form-input', 'placeholder': '0-846'}), required=True)
    bmi = forms.FloatField(label='BMI', widget=forms.NumberInput(
        attrs={'class': 'form-input', 'placeholder': '0-67.0'}), required=True)
    diabetes = forms.FloatField(label='Diabetes Pedigree Function', widget=forms.NumberInput(
        attrs={'class': 'form-input', 'placeholder': '0-2.5'}), required=True)
    age = ""

    class Meta:
        model = ResultsModel
        fields = (
            'pregnancy',
            'glucose',
            'blood_p',
            'skin',
            'insulin',
            'bmi',
            'diabetes',
            'age'
        )

    def save(self, commit=True):
        result = super(AddResultForm, self).save(commit=False)
        result.patient_name = self.cleaned_data['patient_name']
        result.patient_surname = self.cleaned_data['patient_surname']
        result.patient_birthday = self.cleaned_data['patient_birthday']
        result.pregnancy = self.cleaned_data['pregnancy']
        result.glucose = self.cleaned_data['glucose']
        result.blood_p = self.cleaned_data['blood_p']
        result.skin = self.cleaned_data['skin']
        result.insulin = self.cleaned_data['insulin']
        result.bmi = self.cleande_date['bmi']
        result.diabetes = self.cleaned_data['diabetes']
        result.age = calculate_age(result.patient_birthday)

        p = PatientProfile(patient_name=result.patient_name, patient_surname=result.patient_surname,
                           patient_birthday=result.patient_birthday)
        r = ResultsModel(pregnancy=result.pregnancy, glucose=result.glucose, blood_p=result.blood_p, skin=result.skin,
                         insulin=result.insulin, bmi=result.bmi, diabetes=result.diabetes, age=result.age)

        if commit:
            p.save()
            r.save()

        return p, r
