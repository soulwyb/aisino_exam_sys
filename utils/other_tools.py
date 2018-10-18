import datetime

# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-15 13:21'

def avlid_datetiem():
    now_time = datetime.datetime.now()
    new_time = now_time + datetime.timedelta(seconds=3600)
    return new_time
