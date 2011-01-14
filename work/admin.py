from django.contrib import admin
from work.models import Photo, Project

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3
    
class ProjectAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

admin.site.register(Project, ProjectAdmin)
    