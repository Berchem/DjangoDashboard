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

from django.conf.urls import url
from SystemUtil import views

urlpatterns = [
    url(r'^cpu_percent$', views.get_cpu_percent),
    url(r'^memory_percent$', views.get_memory_percent),
    url(r'^recv_speed$', views.get_recv_speed),
    url(r'^battery_status$', views.get_battery_level),

]