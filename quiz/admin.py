from django.contrib import admin
from .models import  Problem, Option

class OptionInline(admin.StackedInline):
    model = Option
    extra = 2

class ProblemAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    
admin.site.register(Problem,ProblemAdmin)
