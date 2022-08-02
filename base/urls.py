from django.urls import path
from base import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('tags/<str:pk>', views.tagPage, name='tag'),
    path('posts/<str:pk>', views.postPage, name='post')
]