# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-11-08 10:37'

from django import forms

class Add_Group_QuestionForm(forms.Form):
    RADIO_CHOICES = (
        ('department', u'部门'),
        ('group', u'组织'),
        ('question', u'题库'),
    )
    input_type = forms.ChoiceField(widget=forms.RadioSelect, choices = RADIO_CHOICES)
    name = forms.CharField(required=True, min_length=4)
    father_group = forms.CharField(required=True)

class Edit_Group_QuestionForm(forms.Form):
    name = forms.CharField(required=True, min_length=4)