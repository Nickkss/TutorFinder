from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from frontend.models import BaseModel
from users.models import User

from PIL import Image

# Create your models here.
class Category(BaseModel):
    name = models.CharField(_("Name"), max_length=500, unique=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        abstract = True

class Blog(BaseModel):
    title = models.CharField(_("Title"), max_length=1000, unique=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True, unique=True, allow_unicode=True)
    image = models.ImageField(_("Feature Image"), upload_to='blog_images/', blank=False)
    content = RichTextField(verbose_name=_("Description"), blank=False)
    
    PUBLISH_CHOICES = [
        (True, "Yes"),
        (False, "No"),
    ]
    publish = models.BooleanField(_("Publish"), default=True, choices=PUBLISH_CHOICES)
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blog_author")
    
    class Meta:
        ordering = ['-created_on']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        try:
            basewidth = 640
            img = Image.open(self.image.path)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img.thumbnail((basewidth, hsize), Image.ANTIALIAS)
            img.save(self.image.path, 'PNG')
        except Exception as ex:
            pass
        
        super().save(*args, **kwargs)