from django.urls import path
from receive_censor_data import views

urlpatterns = [
    path('send/', views.send),
]