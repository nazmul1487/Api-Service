from django.contrib import admin
from django.urls import path
from api.views import UserLoginView, DataInput, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('', DataInput.as_view(), name="data"),
]
