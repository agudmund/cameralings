from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]