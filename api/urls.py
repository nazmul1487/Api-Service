from django.contrib import admin
from django.urls import path
from api.views import LoginView

urlpatterns = [
    path('login/',LoginView, name="login"),
]