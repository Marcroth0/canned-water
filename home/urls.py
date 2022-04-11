
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:product_id>', views.featured_details, name='featured_details'),
    # path('add_to_wish_list/<int:product_id>', views.add_to_wish_list, name='add_to_wish_list'),
    # path('delete_wishlist_item/<int:product_id>', views.delete_wishlist_item, name='delete_wishlist_item'),

]

