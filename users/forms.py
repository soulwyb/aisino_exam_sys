# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-11 13:26'

from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required':u'用户名不为空'})
    password = forms.CharField(required=True, min_length=5, error_messages={
        'required':u'密码不能为空',
        'min_length':u'密码过短'
    })

class ForgetForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '用户名不能为空'})
    captcha = CaptchaField()

class ActiveForm(forms.Form):
    captcha = CaptchaField()
