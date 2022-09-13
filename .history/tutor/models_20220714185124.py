from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.query_utils import Q
from django.urls import reverse
from multiselectfield import MultiSelectField

from frontend.models import BaseModel
from language.models import LangLevel

import random
import string
import os

# Create your models here.
DAY_CHOICES = [
    (1, "Mon"),
    (2, "Tue"),
    (3, "Wed"),
    (4, "Thu"),
    (5, "Fri"),
    (6, "Sat"),
    (7, "Sun"),
]
  

class Tutor(BaseModel):
    name = models.CharField(_("Name"), max_length=500, blank=False)
    email = models.EmailField(_("Email"), blank=False)
    phone = PhoneNumberField(null=True, blank=True, region="IN", verbose_name=_("Mobile No.")) #as_e164
    avtar = models.ImageField(_("Avtar Image"), upload_to="tutor_avtar_uploads/", default="tutor_avtar_uploads/default.png", blank=True)
    
    intro_video = models.FileField(_("Upload Intro Video"), upload_to="tutor_intro_videos/", blank=True, null=True)
    charges = models.PositiveIntegerField(_("Charges per hour"), default=100, help_text=_("Charges in INR"), blank=True)
    about_me = models.TextField(_("About Me"), blank=True, null=True)
    i_speak = models.ManyToManyField(LangLevel, related_name="i_speak", blank=True)
    days_avail = MultiSelectField(choices=DAY_CHOICES, verbose_name=_("Days Available"), blank=False, null=True)
    qualification = models.TextField(_("Qualification"), blank=True, null=True)
    
    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_on']