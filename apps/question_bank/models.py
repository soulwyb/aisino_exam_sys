# encoding:utf-8
from datetime import datetime

from django.db import models

from organization.models import Company, Department, Group

# Create your models here.

#考试题库
class QuestionBank(models.Model):
    company = models.ForeignKey(Company, null = True, blank = True, verbose_name=u'公司', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null = True, blank = True, verbose_name=u'部门', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null = True, blank= True, verbose_name=u'组织', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u'名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'题库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#题目内容
class Questions(models.Model):
    DEGREE_CHOICES = (
        ('cj', u'初级'),
        ('zj', u'中级'),
        ('gj',u'高级'),
    )
    VALID_CHOICES = (
        ('true', u'有效'),
        ('false', u'无效'),
    )
    TYPE_CHOICES = (
        ('dx', u'单选'),
        ('dx', u'多选'),
        ('pd', u'判断')
    )
    questionbank = models.ForeignKey(QuestionBank, verbose_name=u'题库', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name=u'题目')
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=5, verbose_name=u'考试难度')
    option_0 = models.CharField(max_length=200, verbose_name='A')
    option_1 = models.CharField(max_length=200, verbose_name='B')
    option_2 = models.CharField(max_length=200, null = True, blank=True, verbose_name='C')
    option_3 = models.CharField(max_length=200, null = True, blank=True, verbose_name='D')
    option_4 = models.CharField(max_length=200, null = True, blank=True, verbose_name='E')
    answer = models.CharField(max_length=4, verbose_name=u'答案')
    valid = models.CharField(choices=VALID_CHOICES, max_length=5, verbose_name=u'是否有效')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    type = models.CharField(choices=TYPE_CHOICES, max_length=5, verbose_name=u'类型')

    class Meta:
        verbose_name = u'单选题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# #考卷
# class Exam_paper(models.Model):
#     name = models.CharField(max_length=100, verbose_name=u'名称')
#     passing_score = models.IntegerField(max_length=3, verbose_name=u'合格分数')
#     redo = models.IntegerField(max_length=4, verbose_name=u'重做次数')
#