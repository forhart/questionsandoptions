from django.db import models

from django.contrib import admin





# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=300)
    asked_date = models.DateField()

    def __unicode__(self):
        return self.title

class Option(models.Model):
    text  = models.CharField(max_length=300)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.text

admin.site.register(Question)
admin.site.register(Option)
