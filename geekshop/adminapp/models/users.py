from authapp.models import ShopUser
from authapp.forms import UpdateForm


class ShopUserAdminEditForm(UpdateForm):
    class Meta:
        model = ShopUser
        fields = '__all__'
