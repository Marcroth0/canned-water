from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserProfile, WishList
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product

from .forms import UserProfileForm

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def profile_account(request):

    return render(request, 'profiles/profile_account.html')

def wish_list(request):
    wishlist = WishList.objects.filter(user=request.user)

    template = 'profiles/wish_list.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)

# def add_to_wish_list(request):
#     console.log("here")
#     if request.method == 'POST':
#         console.log(request.data)
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
