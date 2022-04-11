
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('quick_view/<product_id>', views.quick_view, name='quick_view'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('delete_review/<int:product_id>/<int:review_id>', views.delete_review, name='delete_review'),
]
