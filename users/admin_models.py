from django.db import models
from django.utils.translation import ugettext_lazy as _

from frontend.models import BaseModel
from .models import User

DB_THEME_CHOICES = [
    ("Theme 1", "bg-theme bg-theme1"),
    ("Theme 2", "bg-theme bg-theme2"),
    ("Theme 3", "bg-theme bg-theme3"),
    ("Theme 4", "bg-theme bg-theme4"),
    ("Theme 5", "bg-theme bg-theme5"),
    ("Theme 6", "bg-theme bg-theme6"),
    ("Theme 7", "bg-theme bg-theme7"),
    ("Theme 8", "bg-theme bg-theme8"),
    ("Theme 9", "bg-theme bg-theme9"),
    ("Theme 10", "bg-theme bg-theme10"),
    ("Theme 11", "bg-theme bg-theme11"),
    ("Theme 12", "bg-theme bg-theme12"),
    ("Theme 13", "bg-theme bg-theme13"),
    ("Theme 14", "bg-theme bg-theme14"),
    ("Theme 15", "bg-theme bg-theme15"),
]

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile", verbose_name=_("User"))
    
    db_theme = models.CharField(_("Dashboard Theme"), choices=DB_THEME_CHOICES, blank=True, default="bg-theme bg-theme1")
    
    def __str__(self):
        return str(self.user.email)