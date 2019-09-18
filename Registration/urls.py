from django.conf.urls import url
from django.contrib.auth import views as auth_views
from Registration import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
