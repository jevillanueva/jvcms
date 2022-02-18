import re
from django import template
from django.utils.safestring import SafeData, mark_safe
from django.utils.text import  normalize_newlines
from django.utils.html import escape
register = template.Library()


@register.filter(name="linebreaksbrclosed")
def linebreaksbrclosed(value):
    return mark_safe(value.replace("\n", "<br/>"))

@register.filter(name="hrclosed")
def hrclosed(value):
    return mark_safe(value.replace("<hr>", "<hr/>"))

@register.filter(name="imageclose")
def imageclose(value):
   
    imgs = re.findall( r'<\s*img[^>]*>',value)
    for img in imgs:
        value = value.replace(img, img[0:-1]+' class="mrkdwnImg"/>')
    return mark_safe(value)

@register.filter(name="specialCharacters")
def specialCharacters(value):
    value = value.replace("{", "&#123;")
    value = value.replace("}", "&#125;")
    return mark_safe(value)