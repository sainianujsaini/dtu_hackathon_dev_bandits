from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from loanlending import settings
# Create your views here.


@login_required
def add_loan_request(request):
        user = request.user
        if request.method=="POST": 
                form = loanrequest(data=request.POST, files=request.FILES)
                if form.is_valid():
                        user_form = form.save(commit=False)
                        user_form.user = user
                        user_form.save()
                        return redirect('/')
        return render(request, 'loanapp/add_loanrequest.html',{'form':loanrequest()})


class ListProducts(ListView):
    template_name = "search_loanrequest.html"
    model = loanrequestspost
    context_object_name = "loanrequestspost"
    paginate_by = 2

PRODUCTS_PER_PAGE = 8
def search_services(request):
    # products = sellerPost.objects.all()
    
    ordering  = request.GET.get('ordering', "")
    search    = request.GET.get('search', "")
    amount    = request.GET.get('amount',"")
    
    if search:
        loanrequests = loanrequestspost.objects.filter(Q(title__icontains=search) | Q(months__icontains=search))
    else:
        loanrequests = loanrequestspost.objects.all()
    if ordering:
        loanrequests = loanrequestspost.objects.all().order_by('-intrest')
        
    if amount:
        loanrequests = loanrequestspost.objects.filter(amount__gt=amount)

#pagination
    page = request.GET.get('page',1)
    loanrequests_paginator = Paginator(loanrequests, PRODUCTS_PER_PAGE)
    try:
        loanrequests = loanrequests_paginator.page(page)
    except EmptyPage:
        loanrequests = loanrequests_paginator.page(loanrequests_paginator.num_pages)
    except:
        loanrequests = loanrequests_paginator.page(PRODUCTS_PER_PAGE)
    return render(request, "loanapp/search_loanrequest.html", {"loanrequests":loanrequests, 'page_obj':loanrequests, 'is_paginated':True, 'paginator':loanrequests_paginator})

def loan_request_page(request,id,*args, **kwargs):
    x = CustomUser.objects.values('id').filter(id=id).first()
    person = loanrequestspost.objects.get(user=x['id'])
    if request.method=="POST": 
                form = loanaccept(request.POST)
                if form.is_valid():
                        user_form = form.save(commit=False)
                        # user_form.accepted_user = request.user.email
                        # user_form.accepted = True
                        user_form.save()
                        current_site = get_current_site(request)
                        mail_subject = "Loan request is Accepted"
                        message =render_to_string('loanapp/accepted_email.html',{
                            'user': x,
                            'auser': request.user,
                            'domain': current_site,
                            
                        })
                        to_email =  x.email
                        print(to_email)
                        send_mail(
                                subject=mail_subject,
                                message=message,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list= [to_email],
                                fail_silently=False,    # if it fails due to some error or email id then it get silenced without affecting others
                            )
                        return redirect('profile/')
    return render(request, "loanapp/loanrequestpage.html",{'person':person,'form':loanaccept()})