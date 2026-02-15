from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Store, Category, Product, Sale, SaleItem


admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleItem)
