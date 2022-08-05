from xml.parsers.expat import model
from django.forms import ModelForm
from base.models import post, profile

class postForm(ModelForm):
    class Meta:
        model = post
        fields = ['name', 'text', 'tags']

class profileForm(ModelForm):
    class Meta:
        model = profile
        fields = '__all__'