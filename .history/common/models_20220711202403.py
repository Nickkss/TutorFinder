from django.db import models
from django.utils.translation import ugettext_lazy as _

from frontend.models import SingletonModel

# Create your models here.
class SiteSettings(SingletonModel):
    title = models.CharField(_("Site Title"), max_length=500)
    logo = models.ImageField(_("Site Logo"), blank=True, null=True, upload_to="site_data/")
    icon = models.ImageField(_("Site Icon"), blank=True, null=True, upload_to="site_data/", help_text=_("Only .png image accepted."))
    
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return "Site Settings"
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"