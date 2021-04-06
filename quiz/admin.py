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
        
    # def get_form(self,request,obj=None,**kwargs):
    #     print(obj,kwargs)
         
    #     return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        
        if not obj.author_id:
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
    list_display = ('quiz','user','score','created_at','get_author')
    readonly_fields =  ('quiz','user','created_at')
    date_hierarchy = 'quiz__created'
    list_filter = ('quiz__schedule_date','quiz__updated')
    search_fields = ('quiz__author__username','quiz__author__email','quiz__author__first_name','quiz__author__last_name',
    'user__username','user__email','user__first_name','user__last_name',
        
    )
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        print(qs)
        if request.user.is_superuser:
            return qs

        return qs.filter(quiz__author=request.user)
    
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "quiz":
    #         kwargs["queryset"] = Quiz.objects.filter(author=request.user)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
    def get_author(self, obj):
        return obj.quiz.author
    get_author.short_description = 'Author'
    get_author.admin_order_field = 'quiz__author'



admin.site.register(ScoreBoard,ScoreBoardAdmin)


