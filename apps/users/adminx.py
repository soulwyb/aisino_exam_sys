# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-09 14:29'

import xadmin

from .models import EmailVerifyRecord, UserProfile

# class UserProfile(object):
#     list_display = ['name', 'ID_num', 'send_type', 'send_time', 'status_time']
#     search_fields = ['code', 'email']
#     list_filter = ['code', 'email', 'send_type', 'send_time', 'status_time']

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time', 'status_time']
    search_fields = ['code', 'email']
    list_filter = ['code', 'email', 'send_type', 'send_time', 'status_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)