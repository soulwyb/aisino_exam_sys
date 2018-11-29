# encoding:utf-8

from itertools import chain
import os
import pandas as pd
from django_pandas.io import read_frame
from sqlalchemy import create_engine
from datetime import datetime
from io import BytesIO

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from organization.models import Company, Department, Group
from question_bank.models import QuestionBank, Questions
from .forms import Add_Group_QuestionForm, Edit_Group_QuestionForm
from aisino_exam_sys.settings import BASE_DIR
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
        questions = Questions.objects.all()[:40]
        # single_question = Single_Choice_Question.objects.filter(questionbank=question_bank)
        # multiple_question = Multiple_Choice_Question.objects.filter(questionbank=question_bank)
        # true_false = True_or_False.objects.filter(questionbank=question_bank)

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
            father_group_id = request.POST.get('name_id', '')
            check = checktype()
            result, grade = check.checktype(father_group, father_group_id)
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
            new_name = request.POST.get('new_name', '')
            old_name_id = request.POST.get('name_id')
            old_name = request.POST.get('old_name', '').strip()
            check = checktype()
            result, grade = check.checktype(old_name, old_name_id)
            if result:
                result.name = new_name
                result.save()
                return HttpResponse('{"status":"success","msg":"修改成功"}', content_type="application/json")
            else:
                que = QuestionBank.objects.filter(Q(name = old_name) & Q(id=int(old_name_id)))[0]
                if que:
                    que.name = new_name
                    que.save()
                    return HttpResponse('{"status":"success","msg":"修改成功"}', content_type="application/json")
                else:
                    return HttpResponse('{"status":"fail","msg":"失败，数据库中找不到这条数据哦。"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail","msg":"错误，亲，数据不对哦"}', content_type="application/json")

class del_group_or_questionView(View,  LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def post(self, request):
        del_form = Edit_Group_QuestionForm(request.POST)
        if del_form.is_valid():
            name = request.POST.get('name', '')
            name_id = request.POST.get('name_id')
            result, grade = checktype.checktype(name, name_id)
            if result:
                result.delete()
                return HttpResponse('{"status":"success","msg":"删除成功。"}', content_type='application/json')
            else:
                try:
                    QuestionBank.objects.filter(Q(name = name) & Q(id=int(name_id)))[0].delete()
                    return HttpResponse('{"status":"success","msg":"删除成功。"}', content_type='application/json')
                except ObjectDoesNotExist:
                    return HttpResponse('{"status":"fail","msg":"对象不存在哦"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"错误，亲，数据不对哦"}', content_type="application/json")


# 过滤题库层级
class checktype:
    def checktype(self,name = '', id = ''):
        if Company.objects.filter(name=name):
            com = Company.objects.filter(Q(name=name) & Q(id=int(id)))[0]
            grade = 1
            return com, grade
        elif Department.objects.filter(name=name):
            dep = Department.objects.filter(Q(name=name) & Q(id=int(id)))[0]
            grade = 2
            return dep, grade
        elif Group.objects.filter(name=name):
            gro = Group.objects.filter(Q(name=name) & Q(id=int(id)))[0]
            grade = 3
            return gro, grade
        else:
            return False, 4

# 导入题库
class upload_question_bankView(View, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def post(self, request):
        xls = request.FILES.get('file', '')
        question_bank = request.POST.get('question_bank_name', '')
        if xls:
            excel_file = pd.read_excel(xls, header = 1)
            if excel_file.empty:
                return HttpResponse('{"status":"fail","msg":"上传文件内容为空，泥煤"}', content_type='application/json')
            elif excel_file[['题目','难度','A','B','答案', '是否有效', '类型']].isnull().any().empty:
                return HttpResponse('{"status":"fail","msg":"Excel表中“题目”“难度”“A”“B”“答案”“是否有效”“类型”含空，请检查后再上传。"}', content_type='application/json')
            else:
                # 整理DataFrame数据
                question = QuestionBank.objects.filter(name=question_bank)[0].id
                print(question)
                times = datetime.now()
                excel_file.insert(10, '所属题库', question)
                excel_file.insert(9, '增加时间', times)
                print(excel_file["难度"].replace(['初级','中级','高级'], ['cj','zj','gj'], inplace=True))
                try:
                    print(excel_file[excel_file["类型"] == 1])
                    excel_file.rename(columns = {'题目':'name', '难度':'degree', 'A':'option_0', 'B':'option_1', 'C': 'option_2', \
                                                'D':'option_3', 'E': 'option_4', '答案':'answer', '是否有效':'valid', \
                                                 '增加时间':'add_time', '类型':'type', '所属题库':'questionbank_id'}, inplace=True)
                    single_question = excel_file[excel_file["type"] == "单选"]
                    multiple_question = excel_file[excel_file["type"] == "多选"]
                    true_or_false_question = excel_file[excel_file['type'] == "判断"]

                except KeyError as e:
                    return HttpResponse('{"status":"fail","msg":"Excel表中的“类型”列没有符合规定的选项"}', content_type='application/json')
                # 写入数据库
                engine = create_engine('mysql+mysqlconnector://root:Aisino@123@localhost:3306/aisino_exam_sys')
                single_question.to_sql(name='question_bank_single_choice_question', con=engine, if_exists='append', index=False)
                multiple_question.to_sql(name='question_bank_multiple_choice_question', con=engine, if_exists='append', index=False)
                true_or_false_question.to_sql(name='question_bank_true_or_false', con=engine, if_exists='append', index=False)
                return HttpResponse('{"status":"success","msg":"题库上传成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"没有文件上传。"}', content_type='application/json')


# 下载题库
class download_questionView(View):
    def get(self, request):
        # question_id = request.POST.get('question_id', '')
        # question = QuestionBank.objects.get(id=int(question_id))
        # questions = read_frame(Questions.objects.filter(questionbank_id=question))
        # out = BytesIO()
        # excels = pd.ExcelWriter(out, engine='xlsxwriter')
        # questions.to_excel(excels, sheet_name = 'Sheet1', index = False, header = False)
        # excels.save()
        # response = HttpResponse(content_type = 'application/vnd.ms-excel')

        excel_file_path = os.path.join(BASE_DIR, 'Media') + r'\题库导入模板.xlsx'
        with excel_file_path as f:
            a = f.read()
        response = HttpResponse(a, content_type='appliaction/vnd.ms-excel')
        return response
        response["Content-Disposition"] = "attachment;filename={0}".format(excel_file_path)
        # response['Content-Disposition'] = 'attachment:filename={}.xlsx'.format(excel_file_path)
        return response
        # questions.to_excel(excel_file_path, sheet_name='Sheet1')
        # file = open(excel_file_path, 'rb')
        # response = FileResponse(file)
        # response['Content-Type'] = 'application/vnd.ms-excel'
        # # response['Content-Disposition'] = 'attachment;filename="{0}"'.format(question.name)
        # response['Content-Disposition'] = 'attachment;filename="1.xlsx"'
        # return response


def downfile(request):
    question_id = request.GET.get('question_id', '')
    question = QuestionBank.objects.get(id=int(question_id))
    questions = read_frame(Questions.objects.filter(questionbank_id=question))
    out = BytesIO()
    excels = pd.ExcelWriter(out, engine='xlsxwriter')
    questions.to_excel(excels, sheet_name = 'Sheet1', index = False, header = False)
    excels.save()
    excel_file_path = os.path.join(BASE_DIR, 'Media') + r'\题库导入模板.xlsx'
    # with open(excel_file_path, 'rb') as f:
    #     a = f.read()
    response = HttpResponse(out.getvalue())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename=1.xlsx'
    return response