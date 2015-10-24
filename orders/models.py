# -*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
    provider_name = models.ForeignKey('auth.User')			# klucz obcy na providera
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    product_description = models.CharField(max_length = 200)
    product_volume = models.IntegerField()
    
    def __str__(self):
        return self.product_name

    """ Moze byc tak, ze danego produktu aktualnei nie ma w ofercie (zapasy wyczerpane)
    Wowczas takiego produktu nie publikujemy. Pytanie tylko jak to sprawdzac (prawdopodobnie 
    potrzebna metoda sprawdzajaca) """
    def publish(self):
        self.save()

class Dormitory(models.Model):
    dormitory_name = models.CharField(max_length = 200)
    dormitory_address = models.CharField(max_length = 200)

    def __str__(self):
        return self.dormitory_name

from django.contrib.auth.models import User, UserManager

class ProviderUser(User):
    
    """User with app settings."""
    provider_dormitory = models.ForeignKey(Dormitory)
    provider_name = models.CharField(max_length = 200)
    provider_phone_number = models.CharField(max_length = 12)
    objects = UserManager()

    def __str__(self):
        return self.provider_name

class CustomerUser(User):
    customer_name = models.CharField(max_length = 100)
    customer_phone_number = models.CharField(max_length = 12)
    customer_orders_number = models.IntegerField()
    customer_orders_value = models.DecimalField(max_digits = 6, decimal_places = 2)
    customer_last_order_date = models.DateTimeField('date of last order')
    objects = UserManager()

    """Metoda sprawdza czy uzytkownikowi nalezy sie odznaka za duza liczbe zamowien"""
    def has_high_orders_number():
    	if customer_orders_number > 10 :
    		return True
        else:
            return False

    """Metoda sprawdza czy uzytkownikowi nalezy sie odznaka za duza wartosc zamowien"""
    def has_high_orders_value():
    	if customer_orders_value > 100.00 :
    		return True
        else:
            return False

    """Jesli klient zamowil cos nie dawniej niz okreslona liczbe dni temu to nalezy sie rabat"""
    def has_recently_ordered():
    	if self.customer_last_order_date >= timezone.now() - datetime.timedelta(days=1):
    		return True
        else:
            return False

    def __str__(self):
        return self.customer_name

