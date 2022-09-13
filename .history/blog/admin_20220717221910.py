from django.contrib import admin

from . import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    
    def author_name(self, instance):
        return str(instance.name)
    
    author_name.short_description = "Author"
    
    list_display = ['title', 'slug', 'publish', 'author_name', 'created_on', 'updated_on']

admin.site.register(models.Blog)