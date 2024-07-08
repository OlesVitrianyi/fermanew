from datetime import datetime

from django import template
from mainapp.models import *

register = template.Library()

# UK у футері в рядку копірайту автоматично виводить поточний рік. Робить код лаконічним без необхідності прописувати
# у кожній функції views.py до кожної сторінки 'current_year': get_current_year,
# EN in the footer in the copyright line automatically displays the current year. Makes the code concise without
# the need to write in each views.py function to each 'current_year' page: get_current_year,


@register.simple_tag
def current_year():
    return datetime.now().year