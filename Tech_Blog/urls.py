from django.contrib import admin
from django.urls import path
from Tech_Blog import views 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('blog/', views.get_Blog, name='blog'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
