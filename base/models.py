from django.db import models
from django.contrib.auth.models import User

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