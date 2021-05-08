from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('input', views.inputs),
    path('result',views.result),
    path('',views.home)
]
