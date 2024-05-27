from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    in_stock = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.price})'
    
class 

