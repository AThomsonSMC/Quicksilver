__author__ = 'adamthomson'

import json

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from Quicksilver.models import Character
from Quicksilver.templatetags import char_filters

STR_SKILLS = ['climb', 'swim']
DEX_SKILLS = ['acrobatics', 'disable', 'escape', 'fly', 'ride', 'sleight', 'stealth']
CON_SKILLS = []
INT_SKILLS = ['appraise', 'craft', 'knowledge', 'linguistics', 'spellcraft']
WIS_SKILLS = ['heal', 'perception', 'profes', 'motive', 'survival']
CHA_SKILLS = ['bluff', 'diplomacy', 'disguise', 'handle_animal', 'intimidate', 'perform', 'use_device']

def index(request):
    """
    :param request:
    :param user_id:
    :return: Character index page info
    """
    characters = get_list_or_404(Character)
    context = {}
    for char in characters:
        context[char.id] = char
    context['message'] = 'Welcome to the Character Index'
    return render(request, 'Quicksilver/character/index.html', context)


def detail(request, char_id):
    """
    :param request:
    :param char_id:
    :return: Character detail page info
    """
    character = get_object_or_404(Character, id=char_id)
    context = {'char': character}
    context['message'] = "Welcome to the details of character %s" %character.name
    return render(request, 'Quicksilver/character/detail.html', context)


def level_up(request, char_id):
    """
    :param request:
    :return:
    """
    character = get_object_or_404(Character, id=char_id)
    context = {'char': character}
    context['message'] = "Level Up %s!" %character.name
    return render(request, 'Quicksilver/character/level_up.html', context)

def char_new(request):
    context = {}
    context['message'] = "Create a new character!"
    return render(request, 'Quicksilver/character/char_new.html', context)


def api_char_list(request):
    all_chars = list(Character.objects.all())

    row_data = []
    for char in all_chars:
        cell_data = []
        char_link = '<a href=/quicksilver/character/%s>' %char.id
        char_link += char.name + '</a>'
        cell_data.append(char_link)
        cell_data.append(char.player.username)
        date_str = '01/01/2015' #TODO:Save character creation date
        cell_data.append(date_str)
        cell_data.append(char.total_level)
        cell_data.append(char.class1.name)
        cell_data.append(char.race.name)
        cell_data.append(char_filters.disp_static(char.alignment, 'align'))
        row_data.append({'id':char.id, 'cell':cell_data})

    results = {'total':'1',
               'page':'1',
               'records':len(row_data),
               'rows': row_data
    }
    json_dict = json.dumps(results)
    return HttpResponse(json_dict, content_type='application/json')


def api_skill_list(request, char_id):
    character = Character.objects.get(id=char_id)

    skill_set = character.skills

    craft1_name   = skill_set.craft1_name
    craft2_name   = skill_set.craft2_name
    perform1_name = skill_set.perform1_name
    perform2_name = skill_set.perform2_name
    profes1_name  = skill_set.profes1_name
    profes2_name  = skill_set.profes2_name

    knowledges = skill_set.knowledges

    skill_list = [
        ('acrobatics', 'Acrobatics'), ('appraise', 'Appraise'), ('bluff', 'Bluff'), ('climb', 'Climb'), ('diplomacy',
        'Diplomacy'), ('disable', 'Disable Device'), ('disguise', 'Disguise'), ('escape', 'Escape Artist'),
        ('fly', 'Fly'), ('handle_animal', 'Handle Animal'), ('heal', 'Heal'), ('intimidate', 'Intimidate'), ('linguistics',
        'Linguistics'), ('perception', 'Perception'), ('ride', 'Ride'), ('motive', 'Sense Motive'), ('sleight',
        'Sleight of Hand'), ('spellcraft', 'Spellcraft'), ('stealth', 'Stealth'), ('survival', 'Survival'), ('swim',
        'Swim'), ('use_device', 'Use Magic Device')
    ]

    if craft1_name:
        skill_list.insert(4, ('craft1', 'Craft (%s)' % craft1_name))
        INT_SKILLS.append('craft1')
    if craft2_name:
        skill_list.insert(5, ('craft2', 'Craft (%s)' % craft1_name))
        INT_SKILLS.append('craft2')
    if perform1_name:
        index = skill_list.index(('perception', 'Perception'))
        skill_list.insert(index+1, ('perform1', 'Perform (%s)' % perform1_name))
        CHA_SKILLS.append('perform1')
    if perform2_name:
        index = skill_list.index(('perception', 'Perception'))
        skill_list.insert(index+1, ('perform2', 'Perform (%s)' % perform2_name))
        CHA_SKILLS.append('perform2')
    if profes1_name:
        index = skill_list.index(('ride', 'Ride'))
        skill_list.insert(index, ('profes1', 'Profession (%s)' % profes1_name))
        INT_SKILLS.append('profes1')
    if profes2_name:
        index = skill_list.index(('ride', 'Ride'))
        skill_list.insert(index, ('profes2', 'Profession (%s)' % profes2_name))
        INT_SKILLS.append('profes2')

    abils = character.ability_scores
    row_data = []
    for index, pair in enumerate(skill_list):
        cell_data = []
        skill_name = pair[1]
        skill_lookup = pair[0]
        skill_abil, abil_mod = _get_skill_abil_mod(skill_lookup, abils)
        #get skill ranks
        skill_ranks = 0
        #get misc_mod
        misc_mod = 0
        total_mod = abil_mod + skill_ranks + misc_mod
        if total_mod >= 0:
            total_str = "+%d" %total_mod
        else:
            total_str = str(total_mod)
        if abil_mod >= 0:
            abil_str = "+%d" %abil_mod
        else:
            abil_str = str(abil_mod)
        cell_data = [skill_name, total_str, skill_abil, abil_str, str(skill_ranks), str(misc_mod)]
        row_data.append({'id':index, 'cell':cell_data})

    results = {
        'total':'1',
        'page':'1',
        'records':len(row_data),
        'rows': row_data
    }

    json_dict = json.dumps(results)
    return HttpResponse(json_dict, content_type='application/json')

def _get_skill_abil_mod(skill_index, abil_set):
    if skill_index in STR_SKILLS:
        return ('STR', abil_set.get_mod('str'))
    elif skill_index in DEX_SKILLS:
        return ('DEX', abil_set.get_mod('dex'))
    elif skill_index in CON_SKILLS:
        return ('CON', abil_set.get_mod('con'))
    elif skill_index in INT_SKILLS:
        return ('INT', abil_set.get_mod('int'))
    elif skill_index in WIS_SKILLS:
        return ('WIS', abil_set.get_mod('wis'))
    elif skill_index in CHA_SKILLS:
        return ('CHA', abil_set.get_mod('cha'))
    else:
        return ('ERR', 0)