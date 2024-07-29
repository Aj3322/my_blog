from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST

from django.contrib.auth import logout
def logout_user(request):
    logout(request)
    return redirect('/')
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'login2.html')
        
        messages.error(request, 'Invalid username or password')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return render(request, 'login2.html')

@require_POST
def register_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        messages.error(request, 'Please correct the error below.')

    return redirect(request.META.get('HTTP_REFERER', '/'))

def get_home(request):
    user_data = None
    if request.user.is_authenticated:
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    return render(request, 'index.html', {'user_data': user_data})
def get_Blog(request):
    return render(request, 'blog.html')
def log_in(request):
    return render(request, 'login2.html')

