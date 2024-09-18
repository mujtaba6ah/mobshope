import datetime
from email.mime import image
from django.db import models

# Create your models here.

# Category of items:
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
# Items model:
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.FloatField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="item_images/")
    # add sale 
    is_sale = models.BooleanField(default= False)
    sale_price = models.FloatField(default=0)

    

    def __str__(self):
        return self.name
    
# Customer model:
class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.EmailField(max_length=100)
    password =  models.CharField(max_length=100)
    phone =  models.CharField(max_length=10)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#  customer Order model:
class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity =  models.IntegerField(default=1)
    address =  models.CharField(max_length=100, default='',blank=True )
    phone = models.CharField(max_length=20,default=True, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item} {self.customer}'
