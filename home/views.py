from django.shortcuts import render
from products.models import Product
from articles.models import Post

def index(request):
    featured = Product.objects.filter(featured_product=True)
    featured_articles = Post.objects.filter(featured_articles=True)
    return render(request, 'home/index.html', {'featured':featured, 'featured_articles':featured_articles})
