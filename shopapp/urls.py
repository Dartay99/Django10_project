from django.urls import path
from .views import *

# path('<Роут маршрут>', <Имя вашей вьюшки>.as_view(), name='<Внутреннее имя для маршрута>'),

urlpatterns = [
    path('items', ItemListView.as_view(), name='item_list_url'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item_detail_url'),
    path('item/create', ItemCreateView.as_view(), name='item_create_url'),
]
