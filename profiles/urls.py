from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('profile_account/', views.profile_account, name='profile_account'),
    path('wishlist/', views.wish_list, name='wish_list'),
    path('add_to_wish_list/<int:product_id>', views.add_to_wish_list, name='add_to_wish_list'),
    path('delete_wishlist_item/<int:product_id>', views.delete_wishlist_item, name='delete_wishlist_item'),
]
