__author__ = 'adamthomson'

from django.shortcuts import render, get_object_or_404, get_list_or_404
from Quicksilver.models import Character

def index(request):
    welcome_message = "Hello!  Welcome to the index."
    context = {'message':welcome_message}
    return render(request, "Quicksilver/index.html", context)