from django.db import models
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

# Create your models here.
