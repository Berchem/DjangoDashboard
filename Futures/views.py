from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from Widgets.views import get_to_do_list
from Futures.models import HModel


# Create your views here.
def redirect(request):
    title = "Dashboard"
    to_do_list = get_to_do_list(request)
    return render(request, 'index.html', locals())


def index(requests):
    return render(requests, 'index.html', locals())


@login_required
def futures(request):
    title = "Futures"
    return render(request, 'futures.html', locals())


def get_data(request):
    data = []
    for record in HModel.objects.all():
        row = dict()
        row["id"] = record.id
        row["date"] = record.date
        row["weighted_index"] = float(record.weighted_index)
        row["volume"] = float(record.volume)
        row["current_price"] = int(record.current_price)
        row["next_price"] = int(record.next_price)
        data += [row]
    return JsonResponse(data, safe=False)


def charts(requests):
    title = "Charts"
    return render(requests, 'charts.html', locals())


def elements(requests):
    title = "UI Elements"
    return render(requests, 'elements.html', locals())


def panels(requests):
    title = "Panels"
    return render(requests, 'panels.html', locals())
