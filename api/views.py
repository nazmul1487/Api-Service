from django.shortcuts import render
import requests


def LoginView(request):
    url = 'https://recruitment.fisdev.com/api/login/'
    payload = {
        "username": "nazmulhassan7489@gmail.com",
        "password": "v0XlCwo65"
    }

    r = requests.post(url, json=payload, )
    data_json = r.json()
    # print( data_json['token'])
    token = data_json['token']
    print(token)

    return render(request, "login.html")