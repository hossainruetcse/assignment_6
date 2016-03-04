from django.contrib import admin
from myapp.models import Question
from myapp.models import Choice


#admin.site.register(Question)
#admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',         {'fields': ['question_text'],'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    inlines= [ChoiceInline]

admin.site.register(Choice)  
admin.site.register(Question, QuestionAdmin)
