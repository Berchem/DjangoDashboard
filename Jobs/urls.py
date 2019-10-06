from django.conf.urls import url
from Jobs import views

urlpatterns = [
    url('^$', views.jobs),
    url(r'^kill/(?P<index>.+)$', views.kill),
]
