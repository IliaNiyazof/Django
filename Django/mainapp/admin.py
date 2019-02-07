from django.contrib import admin
from .models import ProductCategory, Product, Person, Department

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Person)
admin.site.register(Department)
