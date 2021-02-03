from django import template

register = template.Library()

@register.filter("cutd")
def cut_(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'The')

# register.filter("cut",cut)
# register.filter('cutd',cut_)
