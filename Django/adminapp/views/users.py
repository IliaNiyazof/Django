from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from adminapp.models.users import PersonEditForm


# @user_passes_test(lambda user: user.is_superuser)
# def index(request: HttpRequest):
#     users_list = ShopUser.objects.all()
#     title = 'Пользователи'
#
#     return render(request, 'adminapp/users/users_index.html', {
#         'objects': users_list,
#         'title': title,
#     })

# @user_passes_test(lambda user: user.is_superuser)
# def create(request: HttpRequest):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = PersonEditForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users_index'))
#     else:
#         user_form = PersonEditForm()
#
#     content = {'title': title, 'update_form': user_form}
#
#     return render(request, 'adminapp/users/update.html', content)




# @user_passes_test(lambda user: user.is_superuser)
# def update(request: HttpRequest, id=None):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=id)
#     if request.method == 'POST':
#         edit_form = PersonEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:users_update', args=[edit_user.pk]))
#     else:
#         edit_form = PersonEditForm(instance=edit_user)
#
#     content = {'title': title, 'update_form': edit_form}
#
#     return render(request, 'adminapp/users/update.html', content)


# @user_passes_test(lambda user: user.is_superuser)
# def delete(request: HttpRequest, id):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=id)
#
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin:users_index'))
#
#     content = {
#         'title': title,
#         'user_to_delete': user
#     }
#
#     return render(request, 'adminapp/users/delete.html', content)


# @user_passes_test(lambda user: user.is_superuser)
# def read(request: HttpRequest, id):
#     model = ShopUser.objects.filter(pk=id)
#
#     return render(request, 'adminapp/users/read.html', {
#         'model': model,
#     })