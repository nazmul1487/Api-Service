import requests
import uuid
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from api.form import LoginForm, UserInfo
from django.conf import settings


class UserLoginView(View):
    template_name = 'login.html'
    form_class = LoginForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.session.has_key('token'):
            return redirect('data')
        else:
            form = self.form_class(initial=self.initial)

            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.data
            # print(data)
            payload = {
                "username": data.get('email'),
                "password": data.get('password')
            }
            url = 'https://recruitment.fisdev.com/api/login/'
            r = requests.post(url, json=payload, )
            data_json = r.json()

            if r.status_code == 200:
                request.session['token'] = data_json['token']
                print(request.session['token'])
                messages.success(request, 'Login Successfully!!')
                return redirect('data')
            else:
                messages.error(request, data_json['message'])
                return redirect('login')
        else:
            return redirect('login')


class UserLogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.session.has_key('token'):
            del request.session['token']
            messages.error(request, 'Logout Successfully!!')
            return redirect('login')
        else:
            return redirect('login')


class DataInput(View):
    template_name = 'dataSubmit.html'
    form_class = UserInfo
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.session.has_key('token'):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            messages.warning(request, 'You have to login for submit your data!!')
            return redirect('login')

    def post(self, request, *args, **kwargs):
        print(self.request.session['token'])
        if request.session.has_key('token'):
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                data = form.data
                immutable = data._mutable
                data._mutable = True
                data['tsync_id'] = str(uuid.uuid1())
                data['cv_file'] = {'tsync_id': str(uuid.uuid1())}
                data._mutable = immutable

                # Data Uploading
                headers = {
                    'content-type': 'application/json',
                    'Authorization': 'Token ' + self.request.session['token'],
                }
                # Test URL
                submit_url = 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'

                # Final Submission URL
                # submit_url = 'https://recruitment.fisdev.com/api/v1/recruiting-entities/'
                r = requests.post(submit_url, json=data, headers=headers)
                data_json = r.json()

                # CV file uploading
                file_headers = {
                    # 'Content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryFfN0gBBt1cBHK7aK',
                    'Authorization': 'Token ' + self.request.session['token'],
                }
                file_upload_url = 'https://recruitment.fisdev.com/api/file-object/{}/'.format(
                    data_json['cv_file']['id'])
                file = request.FILES['file']
                # file_name = str(file)
                with open(f'{settings.MEDIA_ROOT}/file.pdf', 'wb+') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                rr = requests.put(file_upload_url, files={'file': open(f'{settings.MEDIA_ROOT}/file.pdf', 'rb')}, headers=file_headers)
                file_data_json = rr.json()
                print(file_data_json)
                if rr.status_code == 200:
                    messages.success(request, 'Data Submitted Successfully!!!')
                    return redirect('data')
                else:
                    messages.error(request, data_json['message'])
            else:
                return redirect('data')
        else:
            return redirect('login')


