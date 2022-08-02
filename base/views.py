from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models import post
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    latest_posts = post.objects.all()[:5]
    
    context = {'posts': latest_posts}
    return render(request, 'home.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error('User does not exist')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error('Invalid login or password.')   
            return redirect('login')
        
    return render(request, 'login.html')
        
def registerPage(request):
    return HttpResponse('register')

def logoutPage(request):
    logout(request)
    return redirect('home')