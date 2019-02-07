from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')  #varchar(30)
    logo = models.ImageField(upload_to='departments', verbose_name='Logo', blank=True)

    def __str__(self):
        return f"{self.name}"




class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')  #varchar(30)
    last_name = models.CharField(max_length=30, verbose_name='Last_name')
    age = models.PositiveIntegerField(verbose_name='Age', default=0)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} {self.last_name}"



class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    category = models.CharField(verbose_name='К какой категории товаров относится?', max_length=30, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')  #varchar(30)
    photo = models.ImageField(upload_to='departments', verbose_name='Logo', blank=True)

    def __str__(self):
        return f"{self.name}"