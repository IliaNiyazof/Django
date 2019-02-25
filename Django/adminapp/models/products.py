from mainapp.models import Product
from django.forms import ModelForm


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
