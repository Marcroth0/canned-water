
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:product_id>', views.featured_details, name='featured_details'),

]
