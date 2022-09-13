from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.query_utils import Q
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
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
  
def get_random_id():
    while True:
        temp = string.ascii_letters + string.digits
        rid = "".join(random.choices(temp, k=10))
        objs = Tutor.objects.filter(id=temp)
        if not objs.exists():
            return rid
        
class Days(models.Model):
    mon = models.BooleanField(_("Monday"), default=False, blank=True)
    tue = models.BooleanField(_("Tuesday"), default=False, blank=True)
    wed = models.BooleanField(_("Wednesday"), default=False, blank=True)
    thu = models.BooleanField(_("Thursday"), default=False, blank=True)
    fri = models.BooleanField(_("Friday"), default=False, blank=True)
    sat = models.BooleanField(_("Saturday"), default=False, blank=True)
    sun = models.BooleanField(_("Sunday"), default=False, blank=True)
    
    class Meta:
        verbose_name = "Days"
        verbose_name_plural = "Days"

class Tutor(BaseModel):
    id = models.CharField(_("id"), max_length=100, unique=True, primary_key=True, editable=False, default=get_random_id)
    name = models.CharField(_("Name"), max_length=500, blank=False)
    email = models.EmailField(_("Email"), blank=False, unique=True)
    phone = PhoneNumberField(null=True, blank=True, region="IN", verbose_name=_("Mobile No.")) #as_e164
    avtar = models.ImageField(_("Avtar Image"), upload_to="tutor_avtar_uploads/", default="tutor_avtar_uploads/default.png", blank=True)
    
    intro_video = models.FileField(_("Upload Intro Video"), upload_to="tutor_intro_videos/", blank=True, null=True)
    charges = models.PositiveIntegerField(_("Charges per hour"), default=100, help_text=_("Charges in INR"), blank=True, validators=[MinValueValidator(100)])
    about_me = models.TextField(_("About Me"), blank=True, null=True)
    qualification = models.TextField(_("Qualification"), blank=True, null=True)
    i_speak = models.ManyToManyField(LangLevel, related_name="i_speak", blank=True)
    # days_avail = MultiSelectField(choices=DAY_CHOICES, verbose_name=_("Days Available"), blank=False, null=True)
    days_avail = models.ManyToManyField(Days, blank=True, related_name="tutor_days", verbose_name=_("Days Available"))
    
    def __str__(self):
        return str(self.name) + " | " + str(self.email)

    class Meta:
        ordering = ['-created_on']