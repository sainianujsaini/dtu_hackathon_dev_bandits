from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from .models_fields import LowercaseEmailField
from django.utils import timezone
from django.core.validators import RegexValidator
from accounts.managers import CustomUserManager
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator
# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    USERNAME_FIELD     = 'email'
    email              = LowercaseEmailField(('email adress'),unique=True)
    # phone_no = models.IntegerField(('phone'),unique=True,default="Null")
    is_staff           = models.BooleanField(default=False)
    is_active          = models.BooleanField(default=True)
    date_joined        = models.DateField(default=timezone.now)
    is_customer        = models.BooleanField(default=True)
    is_loanProvider = models.BooleanField(default=False)
    fields=[email]
    EMAIL_FIELD        = 'email'
    phone_regex        = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone              = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()
    
class comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
        
class Userpost(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default=" ",upload_to='media/dynamic/img/user_image',validators=[FileExtensionValidator( ['png','jpg'] )])
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
        )
    comments = models.ForeignKey(comments, on_delete=models.CASCADE)
    
    
class fundraiser(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank = True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default=" ",upload_to='dynamic/img/user_image',validators=[FileExtensionValidator( ['png','jpg'] )])
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(1000000000), MinValueValidator(1)]
        )
    amount_received = models.IntegerField(default=0,validators=[MaxValueValidator(1000000000), MinValueValidator(0)])
    
    @property
    def current_amount(self):
        return self.amount - self.amount_received
    
    def __str__(self):
        return self.title + " i want more $" +str(self.current_amount)

        

