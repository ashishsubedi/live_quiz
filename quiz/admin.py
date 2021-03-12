from django.contrib import admin


from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import  Problem, Option, Quiz, ScoreBoard

admin.site.site_header = "Live Quiz Admin"
admin.site.site_title = "Live Quiz Admin Portal"
admin.site.index_title = "Welcome to Live Quiz Admin Portal"

class OptionInline(NestedTabularInline):
    model = Option
    extra = 4

class ProblemInline(NestedStackedInline):
    model = Problem
    extra = 3
    show_change_link = True
    inlines = [OptionInline]

    
class QuizAdmin(NestedModelAdmin):
    readonly_fields = ['author']
    list_display = ('title','author','status','schedule_date')
    list_filter = ('author','schedule_date','author__is_superuser')
    inlines = [ProblemInline]
        
    def save_model(self, request, obj, form, change):
        print(change)
        if not obj.author:
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
    list_display = ('quiz','user','score')
    
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


