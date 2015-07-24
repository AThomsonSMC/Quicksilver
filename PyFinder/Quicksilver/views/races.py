import json

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from Quicksilver.models import Character
from Quicksilver.templatetags import char_filters

def index(request):
    context = {}
    context['message'] = "Create a new character!"
    return render(request, 'Quicksilver/races/index.html', context)