__author__ = 'adamthomson'

import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from Quicksilver.templatetags import char_filters
from Quicksilver.models import Character, Class, ALIGNMENT_CHOICES, FULL_ALIGNMENT_GRID


def index(request):
    """
    :param request:
    :param user_id:
    :return: Character index page info
    """
    classes = get_list_or_404(Class)
    context = {}
    for cls in classes:
        context[cls.id] = cls
    context['message'] = 'Welcome to the Character Index'

    return render(request, 'Quicksilver/classes/index.html', context)


def detail(request, class_id):
    """
    :param request:
    :param char_id:
    :return: Character detail page info
    """
    char_class = get_object_or_404(Class, id=class_id)
    context = {'class': char_class}
    context['message'] = "Welcome to the details of character %s" %char_class.name
    return render(request, 'Quicksilver/classes/detail.html', context)

def new_class(request):
    context = {}
    context['message'] = "Create a new character!"
    return render(request, 'Quicksilver/classes/new_class.html', context)


def api_class_list(request):
    all_classes = list(Class.objects.all())

    row_data = []
    for class_obj in all_classes:
        cell_data = []
        class_link = '<a href=/quicksilver/class/%s>%s</a>' %(class_obj.id, class_obj.name)
        cell_data.append(class_link)
        align_str = ""
        for choice in ALIGNMENT_CHOICES:
            if class_obj.alignment == choice[0]:
                align_str = choice[1]
        if not align_str:
            if ',' in class_obj.alignment:
                align_str = class_obj.alignment
            else:
                align_choices = zip(*FULL_ALIGNMENT_GRID)
                align_index = align_choices[0].index(class_obj.alignment)
                align_str += align_choices[1][align_index]
        cell_data.append(align_str)
        cell_data.append("d"+str(class_obj.hit_die))
        rank_str = str(class_obj.skill_ranks) + " + [Int]"
        cell_data.append(rank_str)
        weapon_profs = zip(*Class.WEAPON_PROFS)
        wep_index = weapon_profs[0].index(class_obj.weapon_prof)
        weapon_str = weapon_profs[1][wep_index]
        armor_profs = zip(*Class.ARMOR_PROFS)
        armor_index = armor_profs[0].index(class_obj.armor_prof)
        armor_str = armor_profs[1][armor_index]
        if 'tower' in class_obj.shield_prof:
            armor_str += ' + Tower Shields'
        elif 'shield' in class_obj.shield_prof:
            armor_str += ' + Shields'
        cast_profs = zip(*Class.CASTER_CHOICES)
        caster_index = cast_profs[0].index(class_obj.caster)
        caster_str = cast_profs[1][caster_index]
        cell_data.append(weapon_str)
        cell_data.append(armor_str)
        cell_data.append(caster_str)
        row_data.append({'id':class_obj.id, 'cell':cell_data})

    total_rows = len(row_data)

    results = {'total':'1',
               'page':'1',
               'records':len(row_data),
               'rows': row_data
    }
    json_dict = json.dumps(results)
    return HttpResponse(json_dict, content_type='application/json')
