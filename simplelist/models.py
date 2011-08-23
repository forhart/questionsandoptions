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

class OptionAdmin(admin.ModelAdmin):
    list_display = ("text","question")
    search_fields = ("text",)

class OptionInline(admin.StackedInline):
    model = Option
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title","asked_date")
    search_fields = ("title",)
    list_filter = ("asked_date",)
    ordering = ("-asked_date",)
    inlines = [OptionInline]


admin.site.register(Question,QuestionAdmin)
#admin.site.register(Option,OptionAdmin)
