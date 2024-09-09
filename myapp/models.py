from email.mime import image
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="item_images/")
    

    def __str__(self):
        return self.name