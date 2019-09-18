from django.conf.urls import url
from Futures import views

urlpatterns = [
    url('^$', views.futures),
    url('^data/', views.get_data),
]
