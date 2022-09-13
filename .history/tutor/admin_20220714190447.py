from django.contrib import admin

from . import models

# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'charges', 'created_on', 'updated_on']

admin.site.register(models.Tutor, TutorAdmin)
