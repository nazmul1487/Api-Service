from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
import requests
from django.views import View
from django.http import HttpResponse

from api.form import LoginForm


class UserLoginView(View):
    template_name = 'login.html'
    form_class = LoginForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.data
            print(data)
            payload = {
                         "username": data['email'],
                         "password": data['password']
                     }
            url = 'https://recruitment.fisdev.com/api/login/'
            r = requests.post(url, json=payload, )
            data_json = r.json()
            token = data_json['token']
            print(token)
            if r.status_code != 402:
                return redirect('login')
            else:
                return token
        else:
            return redirect('login')




# def LoginView(request):
#     url = 'https://recruitment.fisdev.com/api/login/'
#     payload = {
#         "username": "nazmulhassan7489@gmail.com",
#         "password": "v0XlCwo65"
#     }
#
#     r = requests.post(url, json=payload, )
#     data_json = r.json()
#     # print( data_json['token'])
#     token = data_json['token']
#     print(token)
#
#     return render(request, "login.ht