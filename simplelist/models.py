from django.db import models

from django.contrib import admin





# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=300)
    asked_date = models.DateField()

    def __unicode__(self):
        return self.title

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title","asked_date")

class Option(models.Model):
    text  = models.CharField(max_length=300)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.text

class OptionAdmin(admin.ModelAdmin):
    list_display = ("text","question")


admin.site.register(Question,QuestionAdmin)
admin.site.register(Option,OptionAdmin)
