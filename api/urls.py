from django.contrib import admin
from django.urls import path
from api.views import UserLoginView, DataInput

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('data/',DataInput.as_view(), name="data"),
]