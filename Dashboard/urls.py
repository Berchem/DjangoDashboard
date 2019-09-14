"""Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from Futures import views
from Registration import views as sign_views

urlpatterns = [
    url('admin/', admin.site.urls),

    # url('^login/$', views.login),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/signup/$', sign_views.signup, name='signup'),


    url('^$', views.redirect),
    # url('^index/$', views.index),  # aka /

    url('^widgets/', include('Widgets.urls')),

    url('^charts/$', views.charts),
    url('^elements/$', views.elements),
    url('^panels/$', views.panels),

]
