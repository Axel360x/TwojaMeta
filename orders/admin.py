from django.contrib import admin

from .models import Product, Dormitory, ProviderUser, CustomerUser

admin.site.register(Product)
admin.site.register(Dormitory)
admin.site.register(ProviderUser)
admin.site.register(CustomerUser)