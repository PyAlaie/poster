from django.contrib import admin
from base.models import post, profile,tag,comment


# Register your models here.
admin.site.register(post)
admin.site.register(tag)
admin.site.register(profile)