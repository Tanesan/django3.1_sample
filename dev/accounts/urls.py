from django.urls import path

from . import views

urlpatterns = [
    path('', views.authentificate_user),
]