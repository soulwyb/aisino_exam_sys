from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'名称')

    class Meta:
        verbose_name = u'公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Department(models.Model):
    Company = models.ForeignKey(Company, verbose_name=u'公司', on_delete= models.CASCADE)
    name = models.CharField(max_length=10, verbose_name=u'名称')

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Group(models.Model):
    company = models.ForeignKey(Company, verbose_name=u'公司名称', on_delete= models.CASCADE)
    department = models.ForeignKey(Department, verbose_name=u'部门', on_delete= models.CASCADE)
    name = models.CharField(max_length=20, verbose_name=u'名称')

    class Meta:
        verbose_name = u'组织'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

