from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserProfile, WishList
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product
from django.http import HttpResponseRedirect

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


@login_required
def add_to_wish_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wish_product = get_object_or_404(WishList, user=request.user.id)

    if product in wish_product.product.all():
        messages.info(request, "It's already in there")
    else:
        wish_product = WishList.objects.create(user=request.user)
        wish_product.product.add(product)
        messages.success(request, "It has been added! ")


    return redirect('/')

@login_required
def delete_wishlist_item(request, product_id):
    
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        wish_product = get_object_or_404(WishList, user=request.user.id)

        if product in wish_product.product.all():
            wish_product.product.delete()
            messages.info(request, "It's gonezo!")
        else:
            wish_product.product.add(product)
            messages.success(request, "Sorry, can't find it...")
    else:
        messages.error(request, "You have to be logged in.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
