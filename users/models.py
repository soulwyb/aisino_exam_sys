from datetime import datetime as dt
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.other_tools import avlid_datetiem
# Create your models here.

class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ('male',u'男'),
        ('female', u'女')
    )
    #姓名
    name = models.CharField(max_length=10, verbose_name=u'姓名')
    #身份证号码
    ID_num = models.CharField(max_length=18, verbose_name=u'身份证号')
    #性别
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'性别')
    #生日
    birthday = models.DateField( null = True, blank= True, verbose_name=u'生日')
    #手机号
    mobile = models.CharField(max_length=11,  default='', verbose_name=u'电话')
    #头像
    image = models.ImageField(upload_to = 'image/%Y/%m', max_length=100, default = u'image/default.jpg', verbose_name=u'头像')
    #入职时间
    Entyr_date = models.DateField( null=True, blank=True, verbose_name=u'入职时间')
    #离职时间
    leavedate = models.DateField(null=True, blank=True, verbose_name=u'离职时间')
    #添加时间
    add_time = models.DateTimeField(default=dt.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register', u'注册'),
        ('forget', u'忘记密码')
    )

    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField( max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=SEND_CHOICES, max_length=10, verbose_name=u'发送类型')
    send_time = models.DateTimeField(default=dt.now, verbose_name=u'发送时间')
    status_time = models.DateTimeField(default=avlid_datetiem, verbose_name=u'有效时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
