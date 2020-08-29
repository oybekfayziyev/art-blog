
from django import template

register = template.Library()

@register.filter
def is_equal(value1, value2):
    print('value1',value1)
    print('value2', value2)
    print(type(value1))
    print(type(value2))
    if value1 == value2:
        print('yes')
        return True
    
    return False