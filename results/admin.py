from django.contrib import admin
from results.models import PatientProfile
from results.models import ResultsModel
# Register your models here.

admin.site.register(PatientProfile)
admin.site.register(ResultsModel)
