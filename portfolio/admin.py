from django.contrib import admin
from portfolio.models import Category, Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass
    
class CategoryAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
