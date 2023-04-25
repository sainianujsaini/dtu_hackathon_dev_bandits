from django.contrib import admin
from django.urls import path, include
from userdetails import views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('createprofile/', views.profile_creation, name='profilecreation'),
    path('profile/', views.profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 