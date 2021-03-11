from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import  Problem, Option, Quiz, ScoreBoard

class OptionInline(NestedTabularInline):
    model = Option
    extra = 4

class ProblemInline(NestedTabularInline):
    model = Problem
    extra = 3
    show_change_link = True
    inlines = [OptionInline]

    
class QuizAdmin(NestedModelAdmin):
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

# class ProblemAdmin(admin.ModelAdmin):
#     inlines = [OptionInline]


# admin.site.register(Problem,ProblemAdmin)
admin.site.register(ScoreBoard)


    

