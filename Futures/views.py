from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def redirect(requests):
    title = "Dashboard"
    return render(requests, 'index.html', locals())


def index(requests):
    return render(requests, 'index.html')


def charts(requests):
    title = "Charts"
    return render(requests, 'charts.html', locals())


def elements(requests):
    title = "UI Elements"
    return render(requests, 'elements.html', locals())


def panels(requests):
    title = "Panels"
    return render(requests, 'panels.html', locals())
