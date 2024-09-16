from django.contrib import admin
from .models import Item,Category,Order,Customer

# Register your models here.
admin.site.register(Item,)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)