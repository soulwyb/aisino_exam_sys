# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-19 13:42'

import xadmin

from .models import QuestionBank, Questions


class QuestionBankAdmin(object):
    list_display = ['company', 'department', 'group', 'name', 'add_time']
    search_fields = ['company', 'department', 'group', 'name']
    list_filter = ['company', 'department', 'group', 'name', 'add_time']

class QuestionsAdmin(object):
    list_display = ['name', 'degree', 'option_0', 'option_1', 'option_2', 'option_3',
                    'option_4', 'answer', 'valid', 'add_time','type']
    search_fields = ['name', 'degree', 'valid','type']
    list_filter = ['name', 'degree', 'option_0', 'option_1', 'option_2', 'option_3',
                    'option_4', 'answer', 'valid', 'add_time','type']

xadmin.site.register(QuestionBank, QuestionBankAdmin)
xadmin.site.register(Questions, QuestionBankAdmin)