from django import template
import datetime

register = template.Library()

UKRAINIAN_MONTHS = {
    1: 'Січень',
    2: 'Лютий',
    3: 'Березень',
    4: 'Квітень',
    5: 'Травень',
    6: 'Червень',
    7: 'Липень',
    8: 'Серпень',
    9: 'Вересень',
    10: 'Жовтень',
    11: 'Листопад',
    12: 'Грудень'
}

@register.filter(name='ukrainian_date')
def ukrainian_date(value):
    if isinstance(value, datetime.date):
        day = value.day
        month = UKRAINIAN_MONTHS[value.month]
        year = value.year
        return f"{day} {month} {year}"
    return value