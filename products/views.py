from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Avg

from .models import Product, Category, ProductReview
from .forms import ProductForm, ReviewForm


def products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Enter something, mate")
                return redirect(reverse("product"))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    reviews = ProductReview.objects.filter(product=product_id).order_by(
        "-content"
    )
    product = get_object_or_404(Product, pk=product_id)

    average = reviews.aggregate(Avg("stars"))["stars__avg"]
    if average is None:
        average = 0
    else:
        average = round(average, 2)

    context = {
        "product": product,
        "reviews": reviews,
        "average": average,
    }

    return render(request, "products/product_detail.html", context)


def add_review(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.content = request.POST["content"]
                data.stars = request.POST["stars"]
                data.user = request.user
                data.product = product
                data.save()
                return redirect(reverse("product_detail", args=[product_id]))
        else:
            form = ReviewForm()
        return render(request, "product_detail", {"form": form})
    else:
        return redirect("account_login")


def delete_review(request, product_id, review_id):

    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        review = ProductReview.objects.get(product=product, id=review_id)
        if request.user == review.user:
            review.delete()
        return redirect(reverse("product_detail", args=[product_id]))
    else:
        return redirect("account_login")


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you are not a superuser.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you are not a superuser.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated item!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please check the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete product from store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you are not a superuser.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
