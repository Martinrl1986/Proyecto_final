from django import template
from django.utils.dateformat import format

register = template.Library()

def format_date(value, date_format="%d-%m-%Y"):
    return format(value, date_format)

def truncate_text(value, max_length=100):
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value