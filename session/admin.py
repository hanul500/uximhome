from django.contrib import admin

# Register your models here.
from .models import NewsPost, ActivityPost

admin.site.register(NewsPost)
admin.site.register(ActivityPost)