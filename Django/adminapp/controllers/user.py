from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from authapp.models import ShopUser


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users/users_index.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/users/update.html'
    fields = ('username', 'age', 'password', 'email', 'first_name', 'avatar')
    success_url = reverse_lazy('admin:users_index')


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/users/update.html'
    fields = ('username', 'age', 'email', 'first_name', 'avatar')
    success_url = reverse_lazy('admin:users_index')

    def get_context_data(self, **kwargs):
        parent_context = super(UserUpdateView, self).get_context_data(**kwargs)
        parent_context['title'] = 'пользователи/создание'

        return parent_context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/users/delete.html'
    success_url = reverse_lazy('admin:users_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object() #получаем пользователя
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

