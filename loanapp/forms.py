from django.forms import ModelForm
from django import forms
from .forms import *
from .models import *

class loanrequest(ModelForm):
    class Meta:
        model = loanrequestspost
        fields = ('title','amount','intrest','months',)
class loanaccept(ModelForm):
    class Meta:
        model = loanrequestspost
        fields = ('accepter_msg',)
    