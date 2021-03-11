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
        
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.author_id = request.user.id
        obj.last_modified_by = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Quiz,QuizAdmin)

class ScoreBoardAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
 
        return qs.filter(quiz__author=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "quiz":
            kwargs["queryset"] = Quiz.objects.filter(author=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        



admin.site.register(ScoreBoard,ScoreBoardAdmin)


    

