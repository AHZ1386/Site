from django.contrib import admin
from .models import Product,Category,Order,Brand

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Brand)