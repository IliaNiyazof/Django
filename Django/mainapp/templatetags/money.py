from django import template

register = template.Library()


@register.filter(name='rubles')
def format_money(string_value):
    return f"{string_value} руб."
