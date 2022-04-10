from django.shortcuts import render, get_object_or_404
from products.models import Product
from articles.models import Post

def index(request):
    featured = Product.objects.filter(featured_product=True)
    featured_articles = Post.objects.filter(featured_articles=True)
    return render(request, 'home/index.html', {'featured':featured, 'featured_articles':featured_articles})

def featured_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    template = "home/featured_quick_view.html"

    return render(request, template, context)
