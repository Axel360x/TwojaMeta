from django.db import models

class Product(models.Model):
    producer = models.ForeignKey('auth.User')			# klucz obcy na providera
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    product_description = models.CharField(max_length = 200)

    def __str__(self):
        return self.product_name

    '''
    Moze byc tak, ze danego produktu aktualnei nie ma w ofercie (zapasy wyczerpane)
    Wowczas takiego produktu nie publikujemy. Pytanie tylko jak to sprawdzac (prawdopodobnie 
    potrzebna metoda sprawdzajaca)
    '''
    def publish(self):
        self.save()

class Dormitory(models.Model):
    dormitory_name = models.CharField(max_length = 200)
    dormitory_address = models.CharField(max_length = 200)

    def __str__(self):
        return self.dormitory_name

'''
class Provider(models.User):
	provider_dormitory = models.ForeignKey(Dormitory)
	provider_name = models.CharField(max_length = 200)
    provider_phone_number = models.IntegerField() 

class Customer(models.User):
    odznaki i inne pierdoly

'''