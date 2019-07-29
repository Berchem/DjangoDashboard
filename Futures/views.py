from django.shortcuts import render


# Create your views here.
def redirect(requests):
    title = "Dashboard"
    return render(requests, 'index.html', locals())


def index(requests):
    return render(requests, 'index.html')


def widgets(requests):
    title = "Widgets"
    return render(requests, 'widgets.html', locals())


def charts(requests):
    title = "Charts"
    return render(requests, 'charts.html', locals())


def elements(requests):
    title = "UI Elements"
    return render(requests, 'elements.html', locals())


def panels(requests):
    title = "Panels"
    return render(requests, 'panels.html', locals())


def login(requests):
    return render(requests, 'login.html')

