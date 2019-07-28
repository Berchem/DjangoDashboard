from django.shortcuts import render


# Create your views here.
def redirect(requests):
    return render(requests, 'index.html')


def index(requests):
    return render(requests, 'index.html')


def widgets(requests):
    return render(requests, 'widgets.html')


def charts(requests):
    return render(requests, 'charts.html')


def elements(requests):
    return render(requests, 'elements.html')


def panels(requests):
    return render(requests, 'panels.html')


def login(requests):
    return render(requests, 'login.html')

