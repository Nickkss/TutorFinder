from django.contrib import admin

from . import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'author', 'created_on', 'updated_on']

admin.site.register(models.Blog)