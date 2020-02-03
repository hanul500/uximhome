from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    
    path('', project_page),
    path('create/', project_create),
    path('<str:project_name>/', project_detail),
    #path('media/', media_upload),

    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
