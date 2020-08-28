from django.db import models

# Create your models here.

class HomePage(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(default=f"my name is {name}")

class AboutMe(models.Model):
    dsc1 = models.CharField(max_length=100)
    dsc2 = models.CharField(max_length=100)
    dsc3 = models.CharField(max_length=100)
    dsc4 = models.CharField(max_length=100)
    dsc5 = models.CharField(max_length=100)
    phoneNum = models.CharField(max_length=50)
    telegramId = models.CharField(max_length=50)
    resume = models.FileField(default="")


class Abilities(models.Model):
    ability1 = models.CharField(max_length=50, default="")
    abil1_percent = models.IntegerField(default=0)
    ability2 = models.CharField(max_length=50, default="")
    abil2_percent = models.IntegerField(default=0)
    ability3 = models.CharField(max_length=50, default="")
    abil3_percent = models.IntegerField(default=0)

