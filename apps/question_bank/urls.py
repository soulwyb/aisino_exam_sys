# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-11-07 13:51'

app_name = 'question_bank'

from django.urls import re_path, path

from question_bank.views import add_group_or_questionView, edit_group_or_questionView, \
    del_group_or_questionView, upload_question_bankView, download_questionView, downfile
urlpatterns = [
    path('add_group_bank/', add_group_or_questionView.as_view(), name='add_group_or_bank'),
    path('edit_group_bank/', edit_group_or_questionView.as_view(), name='edit_group_or_bank'),
    path('del_group_bank/', del_group_or_questionView.as_view(), name='del_group_or_bank'),
    path('upload_bank/', upload_question_bankView.as_view(), name="upload_bank"),
    path('download_bank/', downfile, name='download_bank')
]