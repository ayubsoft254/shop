from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    in_stock = models.IntegerField()
    image = models.ImageField(upload_to='media/images')

    def __str__(self):
        return f'{self.name} ({self.price})' 
       
class Customer(models.Model):    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/images')
    

    def __str__(self):
        return f'{self.first_name}'
    
class Order(models.Model):    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()       
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer} | {self.order_date}'
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return f'{self.order}|{self.product}|{self.quantity}'