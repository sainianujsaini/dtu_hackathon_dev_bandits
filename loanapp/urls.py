from django.contrib import admin
from django.urls import path, include
from loanapp import views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('add_loanrequest/', views.add_loan_request, name='add_loanrequest'),
    path('search_loanrequest/', views.search_services, name='search_loan'),
    path('loanrequest/<int:id>', views.loan_request_page, name='search_loan'),
    
    
]
 