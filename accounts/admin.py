from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *



    
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(fundraiser)





