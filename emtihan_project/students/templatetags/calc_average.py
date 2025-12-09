from django import template
register = template.Library()
@register.filter
def calc_average(info):
    try:
        e1 = float(info.get("1-емтихан", 0) or 0)
        e2 = float(info.get("2-емтихан", 0) or 0)
        return (e1 + e2) / 2
    except:
        return 0
