__author__ = 'adamthomson'

from django.shortcuts import render, get_object_or_404, get_list_or_404
from Quicksilver.models import Character

def index(request):
    """
    :param request:
    :param user_id:
    :return: Character index page info
    """
    characters = get_list_or_404(Character)
    context = {}
    for char in characters:
        context[char.name] = char
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