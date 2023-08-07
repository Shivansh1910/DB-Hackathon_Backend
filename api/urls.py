from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('users/', views.getUsers),
    path('user/', views.getUser),
]
