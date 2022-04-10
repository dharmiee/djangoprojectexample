#For Custome Template filters

from pipes import Template
from django import template

register = Template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg,'')  #This cut out all the values"arg" from the string


#register.filter('cut', cut)