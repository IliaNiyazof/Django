from django.contrib import admin
from .models import Department, Person, ProductCategory

# Register your models here.
admin.site.register(Department)
admin.site.register(Person)
admin.site.register(ProductCategory)