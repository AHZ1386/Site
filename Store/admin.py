from django.contrib import admin
from .models import Product,Category,Order,Brand,Comment,OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(OrderItem)
