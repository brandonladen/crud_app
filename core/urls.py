from django.urls import path
from .views import index, create_contact, edit_contact, read_contact, delete_contact

urlpatterns = [
    path('', index, name='home'),
    path('create/', create_contact, name='create'),
    path('edit/<int:c_id>', edit_contact, name='edit'),
    path('read/<int:c_id>', read_contact, name='read'),
    path('delete/<int:c_id>', delete_contact, name='delete'),
]
