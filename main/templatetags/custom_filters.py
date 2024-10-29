from django import template

register = template.Library()

@register.filter(name='startswith')
def startswith(value, arg):
    """
    Returns True if the value starts with the argument.
    Usage: {% if request.path|startswith:"/services/" %}active{% endif %}
    """
    if isinstance(value, str) and isinstance(arg, str):
        return value.startswith(arg)
    return False
