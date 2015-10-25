# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_products/(?P<provider_name>\w+)', views.show_products),
    url(r'^show_providers/(?P<dormitory_name>\w+)', views.show_providers),
    url(r'^show_contact/(?P<provider_name>\w+)', views.show_contact),
    url(r'^show_dormitories', views.show_dormitories),

    url(r'^formularz', views.get_name),

]