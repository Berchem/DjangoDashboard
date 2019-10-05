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
from django.conf.urls import url, include
from Dashboard import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('Registration.urls')),
    url('^widgets/', include('Widgets.urls')),
    url('^conf/', include('Configurations.urls')),
    url('^jobs/', include('Jobs.urls')),
    url('^futures/', include('Futures.urls')),

    url('^$', views.redirect),



    # backend
    url('^charts/$', views.charts),
    url('^elements/$', views.elements),
    url('^panels/$', views.panels),

]
