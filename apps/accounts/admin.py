from django.contrib import admin
from apps.accounts.models import NormalLogin
from django import forms
# Register your models here.



# class NormalLoginForm(forms.ModelForm):
#   class Meta:
#     model = Stop
#     widgets = {
#       'password': ApproveStopWidget(),
#     }
#     fields = '__all__'

# class StopAdmin(admin.ModelAdmin):
#   form = StopAdminForm
admin.site.register(NormalLogin)