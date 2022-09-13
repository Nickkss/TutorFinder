from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(name="check_day_avail")
def check_day_avail(days_avail, day):
    if str(day) in days_avail:
        return True
    return False
    #_days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
    #return _days[int(day)]