from django.urls import path
from . import views

app_name='item'

urlpatterns= [
    path('', views.items, name='items'),
    path('create-item/',views.createItem,name="create-item"),
    path('<int:pk>/',views.detail,name="item"),
    path('edit/<int:pk>/',views.editItem,name="edit"),
    path('delete/<int:pk>/',views.deleteItem,name="delete"),
]