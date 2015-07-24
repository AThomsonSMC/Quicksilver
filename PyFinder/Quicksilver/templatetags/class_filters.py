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
        return 'N/A'
    except:
        return value

@register.filter
def class_static(value, arg):
    try:
        if arg == 'weapon':
            weap_static = models.Class.WEAPON_PROFS
            for option in weap_static:
                if value == option[0]:
                    return option[1]
            return value
        elif arg == 'armor':
            armor_static = models.Class.ARMOR_PROFS
            for option in armor_static:
                if value == option[0]:
                    return option[1]
            return value
        elif arg == 'shield':
            shield_static = models.Class.SHIELD_PROFS
            for option in shield_static:
                if value == option[0]:
                    return ', '+option[1]
            return value
        else:
            return value
    except:
        return value
