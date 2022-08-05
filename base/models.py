from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class tag(models.Model):
    name = models.CharField(max_length=300)
    describtion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class post(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tag, blank=True, null=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name 
    
class comment(models.Model):
    text = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(post, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.text[0:20]
    
class profile(models.Model):
    genders = [
        ('N', 'Rather not to say'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars')
    full_name = models.CharField(max_length=100,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, default='N', choices=genders)
    country = CountryField(null=True, blank=True)
    related_user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.related_user.username