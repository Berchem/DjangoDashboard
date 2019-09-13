import os
import time
import psutil
import datetime as dt

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from SystemUtil.views import get_to_do_list


# Create your views here.
def redirect(request):
    title = "Dashboard"
    to_do_list = get_to_do_list(request)
    return render(request, 'index.html', locals())


def index(requests):
    return render(requests, 'index.html', locals())


def charts(requests):
    title = "Charts"
    return render(requests, 'charts.html', locals())


def elements(requests):
    title = "UI Elements"
    return render(requests, 'elements.html', locals())


def panels(requests):
    title = "Panels"
    return render(requests, 'panels.html', locals())
