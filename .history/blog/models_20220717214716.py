from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from frontend.models import BaseModel

# Create your models here.
class Blog(BaseModel):
    title = models.CharField(_("Title"), max_length=1000)