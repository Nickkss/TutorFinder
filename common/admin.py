from django.contrib import admin

from . import models
# Register your models here.

class SSAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo', 'icon', 'created_on', 'updated_on']

admin.site.register(models.SiteSettings, SSAdmin)