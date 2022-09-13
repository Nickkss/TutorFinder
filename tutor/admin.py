from django.contrib import admin

from . import models

# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'email', 'phone', 'charges', 'created_on', 'updated_on']
    search_fields = ('id', 'name', 'email', 'phone', 'charges')
    list_filter = ['i_speak', 'created_on', 'updated_on']

admin.site.register(models.Tutor, TutorAdmin)
