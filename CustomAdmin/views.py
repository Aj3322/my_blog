from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def adminn_logins(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(username=username, password=password)
        
        if user_obj is not None and user_obj.is_superuser:
            login(request, user_obj)
            return redirect('/dashboard/')
        
        messages.info(request, 'Invalid username or password')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return render(request, 'login2.html')



        
        
        
    
