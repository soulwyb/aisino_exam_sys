from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QuestionBank
from organization.models import Company, Department, Group
# Create your views here.


class question_manageView(View, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def get(self, request):
        companys = Company.objects.all()
        derpartments = Department.objects.all()
        groups = Group.objects.all()
        

        return render(request, 'question-manage.html', {
            'companys': companys,
            'derpartments': derpartments,
            'groups': groups
        })