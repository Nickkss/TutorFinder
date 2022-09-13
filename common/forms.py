from django import forms
from django.conf import settings

from PIL import Image

from . import models

class SiteSettingsForm(forms.ModelForm):
    icon = forms.FileField(widget=forms.FileInput(attrs={'accept':".png"}), required=False)
    class Meta:
        model = models.SiteSettings
        fields = "__all__"
        
           
    def clean_site_logo(self):
        image = self.cleaned_data.get('logo')
        if image:
            format = Image.open(image.file).format
            image.file.seek(0)
            if format in settings.VALID_IMAGE_FILETYPES:
                return image
        raise forms.ValidationError("This image extension is not allowed to upload, please contact developer.")

    
    def clean_site_icon(self):
        image = self.cleaned_data.get('icon')
        if image:
            format = Image.open(image.file).format
            image.file.seek(0)
            if format == 'PNG':
                return image
        raise forms.ValidationError("Invalid image file type detected, please use suggested image format.")