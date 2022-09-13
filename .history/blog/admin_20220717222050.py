from django.contrib import admin

from . import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    
    def author_name(self, instance):
        return str(instance.name)
    
    author_name.short_description = "Author"
    
    list_display = ['title', 'slug', 'publish', 'author_name', 'created_on', 'updated_on']
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(models.Blog)