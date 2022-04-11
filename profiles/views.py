from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserProfile, WishList
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product
from django.http import HttpResponseRedirect, Http404

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
    
@login_required
def profile_account(request):

    return render(request, 'profiles/profile_account.html')

@login_required
def wish_list(request):
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishList.objects.filter(user_wish=user)
    

    template = 'profiles/wish_list.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wish_list(request, product_id):
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        WishList.objects.create(
            user_wish=user,
            product=product
        )
    else:
        messages.error(request, "Sorry, you're not logged in.")

    context = {
        'from_profile': True,
    }
    messages.success(
        request, 'It has been added!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), context)

@login_required
def delete_wishlist_item(request, product_id):
    
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        WishList.objects.filter(product=product, user_wish=user).delete()
        messages.success(
        request, 'It is gonezo!')
    else:
        messages.error(request, "Sorry, you're not logged in.")
        
    context = {
        'from_profile': True,
    }

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), context)
