from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

class HomePage(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    discription = models.TextField(default=f"my name is {name}", verbose_name='توضیحات')
    
    class Meta:
        verbose_name = 'صفحه اصلی'
        verbose_name_plural = 'صفحات اصلی'

class AboutMe(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name='نام')
    dsc1 = models.CharField(max_length=100, verbose_name='توضیح 1')
    dsc2 = models.CharField(max_length=100, verbose_name='توضیح 2')
    dsc3 = models.CharField(max_length=100, verbose_name='توضیح 3')
    dsc4 = models.CharField(max_length=100, verbose_name='توضیح 4')
    dsc5 = models.CharField(max_length=100, verbose_name='توضیح 5')
    phoneNum = models.CharField(max_length=50, verbose_name='شماره تماس')
    telegramId = models.CharField(max_length=50, verbose_name='آیدی تلگرام')
    resume = models.FileField(default="", verbose_name='رزومه')

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'تمامی درباره من'


class Abilities(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name='نام')
    ability1 = models.CharField(max_length=50, default="", verbose_name='توانایی 1')
    abil1_percent = models.IntegerField(default=0, verbose_name='میزان توانایی 1')
    ability2 = models.CharField(max_length=50, default="", verbose_name='توانایی 2')
    abil2_percent = models.IntegerField(default=0, verbose_name='میزان توانایی 2')
    ability3 = models.CharField(max_length=50, default="", verbose_name='توانایی 3')
    abil3_percent = models.IntegerField(default=0, verbose_name='میزان توانایی 3')

    class Meta:
        verbose_name = 'توانایی '
        verbose_name_plural = 'توانایی ها '

