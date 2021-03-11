from django.contrib import admin
from .models import  Problem, Option, Quiz

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class ProblemInline(admin.TabularInline):
    model = Problem
    extra = 3
    show_change_link = True

    
class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ['author']

    inlines = [ProblemInline]
    exclude = ['slug']

    def get_form(self, request, obj=None, **kwargs):  
        Quiz.author = request.user
        return super().get_form(request, obj, **kwargs)
        
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.author_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()

admin.site.register(Quiz,QuizAdmin)

class ProblemAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Problem,ProblemAdmin)
