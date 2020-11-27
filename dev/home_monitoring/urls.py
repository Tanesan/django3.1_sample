from django.urls import path

from . import views
from django.views.generic.base import TemplateView # new
urlpatterns = [
    path('dashboard/', views.index, name='index'),
    # path('dashboard/shower', views.shower), 
    # path('dashboard/toilet', views.toilet), 
    # path('dashboard/curtain', views.curtain), 
    path('send/', views.send),
]