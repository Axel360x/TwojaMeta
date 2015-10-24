from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^choose_shop/(?P<dormitory_name>\w+)', views.choose_shop),
    url(r'^show_contact/(?P<shop_name>\w+)', views.show_contact),
    url(r'^show_products/(?P<shop_name>\w+)', views.show_products),

]

