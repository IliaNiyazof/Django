from authapp.models import ShopUser
from django.forms import ModelForm


class PersonEditForm(ModelForm):
    class Meta:
        model = ShopUser
        fields = '__all__'
