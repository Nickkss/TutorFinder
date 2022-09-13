from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from frontend.models import BaseModel
from users.models import User

import random, string

# Create your models here.
def get_random_id():
    while True:
        temp = string.ascii_letters + string.digits
        rid = "".join(random.choices(temp, k=10))
        language = Language.objects.filter(id=temp)
        if not language.exists():
            return rid
        
class Language(BaseModel):
    id = models.CharField(_("id"), max_length=100, unique=True, primary_key=True, editable=False, default=get_random_id)
    name = models.CharField(_("Language Name"), max_length=200, unique=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True, unique=True, allow_unicode=True)
    
    def clean(self):
        self.name = self.name.capitalize()
        print("Language.objects.filter(name=self.name).exists() = ", Language.objects.filter(name=self.name).exists())
        if Language.objects.filter(name=self.name).exists():
            raise ValidationError(f"Language {self.name} Already Exists!")
        super().clean()
        
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        
def get_random_id():
    while True:
        temp = string.ascii_letters + string.digits
        rid = "".join(random.choices(temp, k=10))
        lang_level = LangLevel.objects.filter(id=temp)
        if not lang_level.exists():
            return rid    
    
class LangLevel(BaseModel):
    id = models.CharField(_("id"), max_length=100, unique=True, primary_key=True, editable=False, default=get_random_id)
    
    tutors = models.ManyToManyField(User, related_name="languages", blank=True)
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="lang_level", verbose_name=_("Select Language"))
    
    LEVEL_CHOICES = [
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Fluent"),
        (4, "Native")
    ]
    level = models.PositiveSmallIntegerField(_("Select Level"), choices=LEVEL_CHOICES, default=1)
    
    def __str__(self):
        return str(self.language.name)
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Language Level"
        verbose_name_plural = "Language Levels"
    