# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-19 13:42'

import xadmin

from .models import QuestionBank, Single_Choice_Question, Multiple_Choice_Question, True_or_False


class QuestionBankAdmin(object):
    list_display = ['company', 'department', 'group', 'name', 'add_time']
    search_fields = ['company', 'department', 'group', 'name']
    list_filter = ['company', 'department', 'group', 'name', 'add_time']


class Single_Choice_QuestionAdmin(object):
    list_display = ['questionbank', 'name', 'degree', 'option_0', 'option_1',
                    'option_2','option_3','option_4', 'answer', 'valid', 'add_time']
    search_fields = ['questionbank', 'name', 'degree', 'option_0', 'option_1',
                    'option_2','option_3','option_4', 'answer', 'valid']
    list_filter = ['questionbank', 'name', 'degree', 'option_0', 'option_1',
                    'option_2','option_3','option_4', 'answer', 'valid', 'add_time']


class Multiple_Choice_QuestionAdmin(object):
    list_display = ['questionbank', 'name', 'degree', 'option_0', 'option_1',
                    'option_2','option_3','option_4', 'answer', 'valid', 'add_time']
    search_fields = ['questionbank', 'name', 'degree', 'option_0', 'option_1',
                    'option_2','option_3','option_4', 'answer', 'valid']
    list_filter = ['questionbank', 'name', 'degree', 'option_0', 'option_1',
                    'option_2','option_3','option_4', 'answer', 'valid', 'add_time']


class Ture_or_FalseAdmin(object):
    list_display = ['questionbank', 'name', 'degree', 'answer', 'valid', 'add_time']
    search_fields = ['questionbank', 'name', 'degree', 'answer', 'valid']
    list_filter = ['questionbank', 'name', 'degree', 'answer', 'valid', 'add_time']

xadmin.site.register(QuestionBank, QuestionBankAdmin)
xadmin.site.register(Single_Choice_Question, Single_Choice_QuestionAdmin)
xadmin.site.register(Multiple_Choice_Question, Multiple_Choice_QuestionAdmin)
xadmin.site.register(True_or_False, Ture_or_FalseAdmin)