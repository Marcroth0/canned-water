from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from articles.models import Post

##temp
from django.contrib import messages
from profiles.models import WishList


def index(request):
    """
    returns home page with featured articles/products
    """
    featured = Product.objects.filter(featured_product=True)
    featured_articles = Post.objects.filter(featured_articles=True)
    return render(
        request,
        "home/index.html",
        {"featured": featured, "featured_articles": featured_articles},
    )


def featured_details(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    template = "home/featured_quick_view.html"

    return render(request, template, context)
