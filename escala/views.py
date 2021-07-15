from django.shortcuts import render

from . import utils
from .models import Place, Schedule


def escala(request):
    place_list, week_schedule = utils.generate_spreadsheet()
    context = {
        'place_list': place_list,
        'week_schedule': week_schedule
    }
    return render(request,'escala/escala.html', context)

