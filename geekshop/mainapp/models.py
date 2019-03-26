from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    logo = models.ImageField(upload_to='departments', verbose_name='Логотип', blank=True)


class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)
    image = models.ImageField(upload_to='users_images', blank=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.department.name}"


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=64)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(db_index=True, verbose_name='активна', default=True)

    productcategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} {self.productcategory.name}"

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('productcategory', 'name')
