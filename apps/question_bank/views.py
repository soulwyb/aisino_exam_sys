# encoding:utf-8

from itertools import chain

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from organization.models import Company, Department, Group
from question_bank.models import QuestionBank, Single_Choice_Question, Multiple_Choice_Question, True_or_False
# Create your views here.


class question_manageView(View, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def get(self, request):
        # if request.user.is_aut
        companys = Company.objects.all()
        derpartments = Department.objects.all()
        groups = Group.objects.all()
        question_bank = QuestionBank.objects.get(id=1)
        single_question = Single_Choice_Question.objects.filter(questionbank=question_bank)
        multiple_question = Multiple_Choice_Question.objects.filter(questionbank=question_bank)
        true_false = True_or_False.objects.filter(questionbank=question_bank)
        questions = chain(single_question, multiple_question, true_false)

        return render(request, 'question-manage.html', {
            'companys': companys,
            'derpartments': derpartments,
            'groups': groups,
            'questions': questions,
        })

    def post(self, request):
        return HttpResponse('{"status":"success"}', content_type="application/json")