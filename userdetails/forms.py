from django.forms import ModelForm
from django import forms
from .forms import *
from accounts .models import *
from .models import *

class userprofiles(ModelForm):
    class Meta:
        model = profilemodel
        fields = ('selfie','first_name','last_name','Bank_Name','Account_Number','CTC','Aadhar_Card','Pan_Card','Pancard_Number','Salary_clip',)

    