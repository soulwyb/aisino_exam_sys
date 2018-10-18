from datetime import datetime

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, ForgetForm, ActiveForm
from utils.send_mail import send_email
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {"msg":"用户名或密码错误！"})
        else:
            return render(request, 'login.html', {'login_form':login_form})


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email = username)|Q(ID_num= username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None

#忘记密码
class ForgetPwdView(View):
    def get(self, request):
        #传验证码过去
        forget_form = ForgetForm()
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        # return render(request, 'forgetpwd.html', {
        #     'forget_form': forget_form
        # })
        return render(request, 'forgetpwd.html', {
            'hashkey': hashkey,
            'image_url': image_url
        })

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        if forget_form.is_valid():
            username = request.POST.get('username', '')
            user = UserProfile.objects.get(username = username)
            send_email(user.email, 'forget')
            return render(request, 'login.html', {'msg':u'重置密码已发送，清注意查收'})
        else:
            return render(request, 'forgetpwd.html', {
                'hashkey': hashkey,
                'image_url': image_url
            })

class ResetPwdView(View):
    def get(self, request, active_code):
        all_recode = EmailVerifyRecord.objects.get(code = active_code)
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        if all_recode:
            if all_recode.status_time > datetime.now():
                email = all_recode.email
                username = UserProfile.objects.get(email = email).username
                return render(request, 'reset-pwd.html', {
                    'username': username,
                    'hashkey': hashkey,
                    'image_url': image_url
                                                          })
            else:
                return render(request, 'forgetpwd.html', {
                    'msg': '验证码失效',
                    'hashkey': hashkey,
                    'image_url': image_url
                })
        else:
            return render(request, 'login.html', {'msg': '验证码错误'})

#重置密码界面的表单POST
class ModifyPwdView(View):
    def post(self, request):
        username = request.POST.get('username', '')
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        resetpwd_form = ActiveForm(request.POST)
        if resetpwd_form.is_valid():
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 != password2:
                return render(request, 'reset-pwd.html', {
                    'username': username,
                    'msg': '密码不一致，请重新输入',
                    'hashkey':hashkey,
                    'image_url': image_url
                })
            else:
                user = UserProfile.objects.get(username = username)
                user.password = make_password(password2)
                user.save()
                request.POST.get('')
                return render(request, 'login.html', {'msg':'密码修改成功，请登录','username':username})
        else:
            return render(request, 'reset-pwd.html',{
                'msg':'验证码错误，请重新输入',
                'username': username,
                'haskey':hashkey,
                'image_url':image_url
            })
