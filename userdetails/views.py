from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

@login_required
def profile_creation(request):
        user = request.user
        if request.method=="POST": 
                form = userprofiles(data=request.POST, files=request.FILES)
                if form.is_valid():
                        user_form = form.save(commit=False)

                        user_form.user = user
                        user_form.save()
                return redirect('/')
        return render(request, 'loanapp/profilecreation.html',{'form':userprofiles()})


def profile(request):
        person = profilemodel.objects.get(user=request.user)  
        print("xxxxxxxxxxxxxxrrrrrrrrrrrrrrrrrrrrrxxxxxxxxxxxxxxxx")
        return render(request, 'loanapp/profile.html',{'person':person})
# for i in images:
#     addprofile.salary_clip = profilemodel.objects.create(
#         user = user,
#         Salary_clip=i,
#     )