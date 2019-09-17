from django.conf.urls import url
from Configurations import views

urlpatterns = [
    url('^$', views.configs),
    url('^test/', views.check),
]