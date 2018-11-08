# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-11-07 13:51'

app_name = 'question_bank'

from django.urls import re_path, path

from question_bank.views import add_group_or_questionView
urlpatterns = [
    path('add_group_bank/', add_group_or_questionView.as_view(), name='add_group_or_bank'),
]