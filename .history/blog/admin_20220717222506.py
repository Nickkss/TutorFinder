from django.contrib import admin

from . import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    
    def author_name(self, instance):
        if instance.author:
            return str(instance.author.name)
        else:
            return "- - - - -"
    
    author_name.short_description = "Author"
    
    list_display = ['title', 'slug', 'publish', 'author_name', 'created_on', 'updated_on']
    search_fields = ('title', 'content', 'author__name')
    list_filter = ['publish', 'created_on', 'updated_on']
    readonly_fields = ('author',)
    exclude_fields = ('author',)
    prepopulated_fields = {"slug": ("title",)}
    
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(models.Blog, BlogAdmin)