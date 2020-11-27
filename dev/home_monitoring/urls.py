from django.urls import path, re_path

from . import views
from django.views.generic.base import TemplateView # new
urlpatterns = [
    path('dashboard/', views.index, name='index'),
    
    path('dashboard/shower', views.shower, name='shower'), 
    path('dashboard/toilet', views.toilet, name='toilet'), 
    path('dashboard/curtain', views.curtain, name='curtain'), 
    path('send/', views.send),
]