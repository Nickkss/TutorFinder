from django.contrib import admin

from . import models

# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    def get_da(self, instance):
        print(instance.days_avail)
        return "Shadow"
    
    list_display = ['id', 'name', 'email', 'phone', 'charges', 'created_on', 'updated_on']
    search_fields = ('id', 'name', 'email', 'phone', 'charges')
    list_filter = ['i_speak', 'days_avail', 'created_on', 'updated_on']

admin.site.register(models.Tutor, TutorAdmin)
