from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
from mainapp.models import ProductCategory
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        # ProductCategory.objects.all().delete()
        #
        # for x in range(5):
        #     new_cat = ProductCategory()
        #     new_cat.save()

        # super_user = User.objects.create_superuser(
        #     'faf', 'test@test.ru', 'root'
        # )

        ShopUser.objects.create_superuser(
            'faf', 'test@test.ru', 'root', age=20
        )
