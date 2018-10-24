# encoding:utf-8
__author__ = 'wuyubin'
__date__ = '2018-10-19 13:39'

import xadmin

from .models import Company, Department, Group

class CompanyAdmin(object):
    list_display = ['name', 'add_time']
    search_fielder = ['name']
    list_filter = ['name', 'add_time']

class DepartmentAdmin(object):
    list_display = ['name', 'company', 'add_time']
    search_fielder = ['name', 'company']
    list_filter = ['name', 'company', 'add_time']

class GroupAdmin(object):
    list_display = ['name', 'department', 'add_time']
    search_fielder = ['name', 'department']
    list_filter = ['name', 'department', 'add_time']

xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Group, GroupAdmin)