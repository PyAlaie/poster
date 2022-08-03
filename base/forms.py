from xml.parsers.expat import model
from django.forms import ModelForm
from base.models import post

class postForm(ModelForm):
    class Meta:
        model = post
        fields = ['name', 'text', 'tags']