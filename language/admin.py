from django.contrib import admin

from . import models, forms

# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_on', 'updated_on']
    search_fields = ('name', )
    list_filter = ('created_on', 'updated_on')
    prepopulated_fields = {"slug": ("name",)}
    
    form = forms.LanguageForm

class LangLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'language']
    
    form = forms.LangLevelForm

admin.site.register(models.Language, LanguageAdmin)

admin.site.register(models.LangLevel, LangLevelAdmin)