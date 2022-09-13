from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.query_utils import Q
from django.urls import reverse
from multiselectfield import MultiSelectField

from frontend.models import BaseModel

import random
import string
import os

# Utils Area Start
mix_vars = string.ascii_letters + string.digits
length = 20

        
def generate_random_number(k=10):
    rnum = "".join(random.choices(string.digits, k=k))
    return rnum
        
def get_random_id():
    while True:
        rid = generate_random_number(k=10)
        try:
            users = User.objects.filter(id=rid)
            if not users.exists():
                return rid
        except Exception as ex:
            return rid

# Utils Area End

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        
        username = str(username).lower()
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(_("id"), max_length=100, unique=True, primary_key=True, editable=False, default=get_random_id)
    username = models.CharField(_("Username"), max_length=100, unique=True)
    name = models.CharField(_("Name"), max_length=1000, null=True, blank=False)
    email = models.EmailField(_('Email Address'), blank=False)
    phone = PhoneNumberField(null=True, blank=True, region="IN", verbose_name=_("Mobile No.")) #as_e164
    avtar = models.ImageField(_("Avtar Image"), upload_to="user_avtar_uploads/", default="user_avtar_uploads/default.png", blank=True)
    
    country = models.CharField(_("Country"), max_length=100, blank=True, null=True)
    state = models.CharField(_("State"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=500, blank=True, null=True)
    
    ROLE_CHOICES = [
        (1, "Tutor"),
        (2, "Student")
    ]
    role = models.SmallIntegerField(_("Role"), choices=ROLE_CHOICES, default=2, help_text=_("Choose User Role"))

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    active_mail_sent = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    objects = UserManager()
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.username)
    
    @property
    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))
    
    @property
    def get_logout_url(self):
        return reverse("users:Logout")
    
    @property
    def profile(self):
        if self.role == 1:
            return self.tutor_profile
        else:
            return self.student_profile
    
    class Meta:
        ordering = ['-last_login']
        verbose_name = "User"
        verbose_name_plural = "All Users"
    
class StudentProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"), related_name="student_profile")
    
    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_on']
        
DAY_CHOICES = [
    (1, "Mon"),
    (2, "Tue"),
    (3, "Wed"),
    (4, "Thu"),
    (5, "Fri"),
    (6, "Sat"),
    (7, "Sun"),
]
        
class TutorProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"), related_name="tutor_profile")
    intro_video = models.FileField(_("Upload Intro Video"), upload_to="tutor_intro_videos/", blank=True, null=True)
    charges = models.PositiveIntegerField(_("Charges per hour"), default=100, help_text=_("Charges in INR"), blank=True)
    about_me = models.TextField(_("About Me"), blank=True, null=True)
    #i_speak = models.TextField(_("I Speak"), blank=True, null=True, help_text=_("Example: Hindi, Korean (Beginner, Intermediate, Fluent, Native)"))
    days_avail = MultiSelectField(choices=DAY_CHOICES, verbose_name=_("Days Available"), blank=False, null=True)
    qualification = models.TextField(_("Qualification"), blank=True, null=True)
    
    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_on']