from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_list, name='business_list'),
]