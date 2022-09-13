from django import template
from django.urls import reverse

register = template.Library()

@register.filter(name="check_path")
def check_path(target,name):
    try:
        url = reverse(name)
        return (target==url)
    except Exception as ex:
        return False

@register.filter(name="enum")
def enum(lst, k=0):
    return enumerate(lst, k)