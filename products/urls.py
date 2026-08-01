from django.urls import path
from . import views

urlpatterns = [

    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    path(
        'products/add/',
        views.add_product,
        name='add_product'
    ),
    path(
        'products/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'products/<int:product_id>/delete/',
        views.delete_product,
        name='delete_product'
    ),
    path(
    'products/all/',
    views.all_products,
    name='all_products'
    ),
    
    path(
    'product/<int:product_id>/',
    views.product_detail,
    name='product_detail'
),
]
