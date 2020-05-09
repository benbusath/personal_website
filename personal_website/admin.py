from django.contrib import admin
from personal_website.models import Image,Resume
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    pass
class ResumeAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Image, ImageAdmin)
admin.site.register(Resume, ResumeAdmin)
