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
from Widgets import views

urlpatterns = [
    url('^$', views.widgets),
    url(r'^system/status$', views.get_system_status),

    url(r'^to_do/update/(?P<index>.+)$', views.update_to_do_status),
    url(r'^to_do/delete/(?P<index>.+)$', views.delete_to_do_item),
    url(r'^to_do/insert/(?P<item>.+)$', views.insert_to_do_list),

    url(r'^chat/insert/(?P<msg>.+)$', views.insert_message),
    url(r'^chat/status$', views.get_chat_status),

]