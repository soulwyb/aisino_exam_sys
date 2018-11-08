# encoding:utf-8

from itertools import chain

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from organization.models import Company, Department, Group
from question_bank.models import QuestionBank, Single_Choice_Question, Multiple_Choice_Question, True_or_False
from .forms import Add_Group_QuestionForm, Edit_Group_QuestionForm
# Create your views here.

# 题库页面
class question_manageView(View, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def get(self, request):
        # if request.user.is_aut
        companys = Company.objects.all()
        departments = Department.objects.all()
        groups = Group.objects.all()
        question_bank = QuestionBank.objects.get(id=1)
        single_question = Single_Choice_Question.objects.filter(questionbank=question_bank)
        multiple_question = Multiple_Choice_Question.objects.filter(questionbank=question_bank)
        true_false = True_or_False.objects.filter(questionbank=question_bank)
        questions = chain(single_question, multiple_question, true_false)

        return render(request, 'question-manage.html', {
            'companys': companys,
            'departments': departments,
            'groups': groups,
            'questions': questions,
        })

# 新增组织部门或者题库
class add_group_or_questionView(View, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def post(self, request):
        add_form = Add_Group_QuestionForm(request.POST)
        if add_form.is_valid():
            input_type = request.POST.get('input_type', '')
            name = request.POST.get('name', '')
            father_group = request.POST.get('father_group', '').strip()
            check = checktype()
            result, grade = check.checktype(father_group)
            if result:
                if input_type == 'department':
                    dep = Department()
                    dep.name = name
                    dep.company = result
                    dep.save()
                    return HttpResponse('{"status":"success","msg":"新建成功"}', content_type='application/json')
                elif input_type == 'group':
                    gro = Group()
                    gro.name = name
                    gro.department = result
                    gro.save()
                    return HttpResponse('{"status":"success","msg":"新建成功"}', content_type='application/json')
                elif input_type == 'question':
                    que = QuestionBank()
                    que.name = name
                    if grade == 3:
                        que.group = Group.objects.filter(name=father_group)[0]
                    elif grade == 2:
                        que.department = Department.objects.filter(name = father_group)[0]
                    elif grade == 1:
                        que.company = Company.objects.filter(name = father_group)[0]
                    que.save()
                    return HttpResponse('{"status":"success","msg":"新建成功"}', content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail", "msg":"组织类型错误哦~，亲不是用网页连接的吧"}', content_type="application/json")
            else:
                return HttpResponse('{"status":"fail", "msg":"亲，不能选题库哦~"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail", "msg":"亲，数据错误，亲不适用网页连接的吧"}', content_type="application/json")

# 编辑组织部门或者题库
class edit_group_or_questionView(View, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def post(self, request):
        edit_form = Edit_Group_QuestionForm(request.POST)
        if edit_form.is_valid():
            name = request.POST.get('name', '')
            father_group = request.POST.get('father_group', '').strip()
            check = checktype()
            result, grade = check.checktype(father_group)
            if result:
                result.name = name
                result.save()
                return HttpResponse('{"status":"success","msg":"修改成功"}', content_type="application/json")
            else:
                que = QuestionBank.objects.filter(name = father_group)[0]
                if que:
                    que.name = name
                    que.save()
                    return HttpResponse('{"status":"success","msg":"修改成功"}', content_type="application/json")
                else:
                    return HttpResponse('{"status":"fail","msg":"失败，数据库中找不到这条数据哦。"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail","msg":"错误，亲，数据不对哦"}', content_type="application/json")



# 过滤题库层级
class checktype:
    def checktype(self,father_group = ''):
        if Company.objects.filter(name=father_group):
            com = Company.objects.filter(name=father_group)[0]
            grade = 1
            return com, grade
        elif Department.objects.filter(name=father_group):
            dep = Department.objects.filter(name=father_group)[0]
            grade = 2
            return dep, grade
        elif Group.objects.filter(name=father_group):
            gro = Group.objects.filter(name=father_group)[0]
            grade = 3
            return gro, grade
        else:
            return False, 4




