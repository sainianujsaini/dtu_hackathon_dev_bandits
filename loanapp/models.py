import re
from django.db import models
from userdetails.models import *
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator
# Create your models here.
from accounts.models import *
from django.core.mail import EmailMessage



class loanrequestspost(models.Model):
    user        = models.OneToOneField(CustomUser,primary_key=True, on_delete=models.CASCADE)
    time_added  = models.DateTimeField(auto_now=True)
    title       = models.CharField(max_length=100,blank=True, null=True)
    accepter_msg= models.TextField(blank=True, null=True)
    accepted    = models.BooleanField(default=False,blank=True, null=True)
    accepted_user = models.CharField(max_length=100, blank=True,null=True) 
    amount      = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(9999999), MinValueValidator(0)]
    )
    intrest = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(3)]
    )
    months= models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(60), MinValueValidator(1)]
    )
    
    class Meta:
        ordering = ['amount']
        
    def get_queryset(self):
        return loanrequestspost.objects.filter(user=self.request.user)
    
    def send_mail(self):
        if(self.accepted):
            pass
        return self.accepted