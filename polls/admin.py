from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
   model =  Choice
   extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',      {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
