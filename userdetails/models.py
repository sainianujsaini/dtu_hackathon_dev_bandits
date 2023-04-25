from django.db import models
from accounts .models import *
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator

# Create your models here.
class profilemodel(models.Model):
    user        = models.OneToOneField(CustomUser,primary_key=True, on_delete=models.CASCADE)
    time_added  = models.DateTimeField(auto_now=True)
    selfie      = models.FileField(default=" ",upload_to = 'images/userprofile/selfie',blank=True, null=True)
    CTC         = models.CharField(max_length=10,blank=True)
    first_name  = models.CharField(max_length=40,blank=True)
    last_name   = models.CharField(max_length=40,blank=True)
    age         = models.IntegerField(
        default=18,
        validators=[MaxValueValidator(100), MinValueValidator(18)]
    )
    years_of_work_experience = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(40), MinValueValidator(0)]
    )
    Bank_Name   = models.CharField(max_length=40,blank=True)
    Account_Number = models.CharField(max_length=16,blank=True)
    cibil_score = models.IntegerField(
        default=500,
        validators=[MaxValueValidator(700), MinValueValidator(500)]
    )
    repayment_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    Aadhar_Card    = models.FileField(upload_to = 'images/userprofile/adharcard',blank=True, null=True)
    Pan_Card       = models.FileField(upload_to = 'images/userprofile/pancard',blank=True, null=True)
    Pancard_Number = models.CharField(max_length=10,blank=True)
    Salary_clip    = models.FileField(upload_to = 'images/userprofile/salarslips',blank=True, null=True)
    
    @property
    def max_loan_month(self):
        total = self.CTC
        can_pay = ((int(total)/12)/10)*3
        return can_pay
    @property
    def cal_cibil_score(self):
        cibil_score = self.cibil_score
        if((self.age>=18 and self.age<=25) and self.years_of_work_experience>3):
            self.repayment_score=50
        if(int(self.CTC)>300000):
            cibil_score+=50
        if(self.age<25 and int(self.CTC)>300000):
            cibil_score+=50
        if(int(self.CTC) > 1200000 and self.years_of_work_experience>5):
            cibil_score+=50
        if(self.repayment_score>0):
            cibil_score+=self.repayment_score
        self.cibil_score=cibil_score
        return cibil_score
    
    def __str__(self):
        return self.first_name + "cibil score is " + str(self.cal_cibil_score)

