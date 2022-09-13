from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from frontend.models import BaseModel
from users.models import User

# Create your models here.
class Blog(BaseModel):
    title = models.CharField(_("Title"), max_length=1000, unique=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True, unique=True, allow_unicode=True)
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blog_author")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super().save(*args, **kwargs)