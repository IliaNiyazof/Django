from django.db import models
from django.conf import settings
from mainapp.models import Product


# Create your models here.
class Basket(models.Model):
    _cost: float
    _total_quantity: int
    _total_cost: float

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во', default=0)
    add_datetime = models.DateTimeField(verbose_name='Дата обновления', auto_now_add=True)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        total = sum([x.quantity for x in items])

        return total

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        total = sum([x.product_cost for x in items])

        return total

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__productcategory')
