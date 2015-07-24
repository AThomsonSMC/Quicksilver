__author__ = 'adamthomson'

from django import template
from Quicksilver import models

register = template.Library()

@register.filter
def disp_static(value, arg):
    try:
        arg_static = models.STATICS[arg]
        for option in arg_static:
            if value == option[0]:
                return option[1]
        return value
    except:
        return value

@register.filter
def abil_mod(value):
    try:
        score = int(value)
        mod = (score-10)/2
        if mod >= 0:
            return "+"+str(mod)
        else:
            return str(mod)
    except:
        return "0"

@register.filter
def save_mod(value, arg):
    save_list = value.split(';')
    save_pairs = [((save.split(':'))[0], (save.split(':'))[1]) for save in save_list]
    for pair in save_pairs:
        if pair[0] == arg:
            return pair[1]