from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_articles, name='view_articles'),
    path('<article_id>', views.article_details, name='article_details'),
    path('add_article_post/', views.add_article_post, name="add_article_post"),
    path('add_article_post/', views.add_article_post, name="add_article_post"),
    path('delete_article_post/<int:blog_id>/', views.delete_article_post, name="delete_article_post"),

]
