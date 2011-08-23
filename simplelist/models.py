from django.db import models

from django.contrib import admin





# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=300)
    asked_date = models.DateField()

class Option(models.Model):
    text  = models.CharField(max_length=300)
    question = models.ForeignKey(Question)



admin.site.register(Question)
admin.site.register(Option)
