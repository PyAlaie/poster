from unicodedata import name
from venv import create
from django.urls import path
from base import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('tags/<str:pk>', views.tagPage, name='tag'),
    path('posts/<str:pk>', views.postPage, name='post'),
    path('posts/<str:pk>/edit', views.editPost, name='editPost'),
    path('new-post/', views.createPost, name='newPost'),
    path('users/<str:username>', views.profilePage, name='profile'),
    path('users/<str:username>/edit', views.profileEdit, name='profileEdit'),
]