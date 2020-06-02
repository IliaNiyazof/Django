# class User:
#     _first_name: str
#     _last_name: str
#
#     def __init__(self, f_name, l_name):
#         self._first_name = f_name
#         self._last_name = l_name
#
#     @property
#     def full_name(self):
#         return f"{self._first_name} {self._last_name}"
#
#     @full_name.setter
#     def full_name(self, value):
#
#     def show_name(self):
#         print(f"User -> {self._first_name} {self._last_name}")
#
#
# john = User(f_name='John', l_name='Doe')
# print(john.full_name)
# john.full_name = 123123