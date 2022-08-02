from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from base.models import comment, post, tag
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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
            messages.error(request, 'User does not exist')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login or password.')   
            return redirect('login')
        
    return render(request, 'login.html')
        
def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error happend during registertion :(')
    context = {'form': form}
    return render(request, 'register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def tagPage(request, pk):
    tag_object = get_object_or_404(tag, id=pk)
    related_posts = tag_object.post_set.all()
    return render(request, 'tag.html', {'tag': tag_object, 'posts': related_posts})

def postPage(request, pk):
    post_object = get_object_or_404(post, id=pk)
    related_comments = comment.objects.filter(post=post_object)
    
    context = {'post':post_object, 'comments': related_comments}
    return render(request, 'post.html', context)