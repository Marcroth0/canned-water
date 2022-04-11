from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from articles.models import Post

##temp
from django.contrib import messages
from profiles.models import WishList

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

# def add_to_wish_list(request):

#     if request.method == "POST":
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             product_check = Product.objects.get(id=prod_id)
#             if(product_check):
#                 if(WishList.objects.filter(user=request.user, product_id=prod_id)):
#                     messages.info(request, 'Product is already in there.')
#                 else:
#                     WishList.objects.create(user=request.user, product_id=prod_id)
#                     messages.success(request, 'Product added to Wishlist.')
#             else:
#                 messages.error(request, 'Sorry, cannot find the product')
#         else:
#             messages.error(request, 'You have to be logged in.')
#     return redirect('/')

# def delete_wishlist_item(request):
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get('product_id'))
#             if(WishList.objects.filter(user=request.user, product_id=prod_id)):
#                 wishlist_item = WishList.objects.get(product_id=prod_id)
#                 wishlist_item.delete()
#                 messages.success(request, 'Product removed from Wishlist.')
#             else:
#                 messages.error(request, 'Product not found.')
#         else:
#             messages.error(request, "You have to be logged in.")
#     return redirect('/')

# def delete_wishlist_item(request, item_id):

#     if request.method == "POST":
# #         if request.user.is_authenticated:
