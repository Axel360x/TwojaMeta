from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^show_providers/(?P<dormitory_name>\w+)', views.show_providers),
    url(r'^show_dormitories/(?P<dormitory_name>\w+)', views.show_dormitories),
    url(r'^show_contact/(?P<shop_name>\w+)', views.show_contact),
    url(r'^show_products/(?P<shop_name>\w+)', views.show_products),

]