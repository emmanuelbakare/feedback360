from django import template

register = template.Library()

@register.filter
def addfield(model, field):

    return getattr(model,field)