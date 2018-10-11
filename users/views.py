from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, ForgetForm
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
        forget_form = ForgetForm()
        return render(request, 'forgetpass.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            username = request.POST.get('username', '')
            user = UserProfile.objects.get(name = username)
            send_email(user.email, 'forget')
            return render(request, 'login.html', {'msg':'重置密码已发送，清注意查收'})
        else:
            return render(request,'forgetpass.html', {'forget_form': forget_form})

class ResetPwdView(View):
    def get(self, request, active_code):
        all_recode = EmailVerifyRecord.objects.get(code = active_code)
