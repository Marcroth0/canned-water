from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_articles, name='view_articles'),
]
