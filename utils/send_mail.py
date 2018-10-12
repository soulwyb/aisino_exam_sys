# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-11 17:38'

from random import Random

from django.core.mail import send_mail, EmailMessage
from aisino_exam_sys.settings import EMAIL_FROM
from django.template.loader import render_to_string

from users.models import EmailVerifyRecord

def random_str(random_length = 8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

def send_email(email, send_type = 'forget'):
    email_record = EmailVerifyRecord()
    code = random_str(10)
    email_record.code = code
    email_record.email = email
    email_record.type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'forget':
        email_title = u'Aisino厦门航信金税业务部忘记密码重置连接'
        email_body = u'请点击一下连接进入重置页面：http://192.168.2.115:8000/acvive/{0}'.format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FROM, [email])

