from django import forms

from django.forms import ValidationError as FormValidationError
from users.models import User

from . import models

class LanguageForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = "__all__"
        
    def save(self, commit=True, *args, **kwargs):
        
        instance = super().save(commit=False, *args, **kwargs)
        
        instance.save()
        return instance
    
class LangLevelForm(forms.ModelForm):
    class Meta:
        model = models.LangLevel
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        tutors = User.objects.filter(role=1)
        self.fields['tutors'].queryset = tutors
        