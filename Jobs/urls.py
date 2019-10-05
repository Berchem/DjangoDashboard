from django.conf.urls import url
from Jobs import views

urlpatterns = [
    url('^$', views.jobs),
]
