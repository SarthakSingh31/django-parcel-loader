from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_bundle(bundle_name):
    return mark_safe(bundle_name)