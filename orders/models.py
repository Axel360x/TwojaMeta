from django.db import models

class Product(models.Model):
    producer = models.ForeignKey('auth.User')
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    product_description = models.CharField(max_length = 200)
    product_type = models.CharField(max_length = 50)

    '''
    Opublikowanie produktu na stronie (udostepnienie mozliwosci zamowienia)
    '''
    def __str__(self):
        return self.product_name

    '''
    Moze byc tak, ze danego produktu aktualnei nie ma w ofercie (zapasy wyczerpane)
    Wowczas takiego produktu nie publikujemy. Pytanie tylko jak to sprawdzac (prawdopodobnie 
    potrzebna metoda sprawdzajaca)
    '''
    def publish(self):
        self.save()

#class Customer(models.Model):