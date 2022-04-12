from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from profiles.models import UserProfile


def contact_us(request):
    """
    View to let users send email to owner of site
    """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your message,\
                              we will be in touch soon",
            )
            return redirect("contact_us")
        else:
            messages.error(
                request,
                "Something went wrong,\
                            Please try again",
            )
            return redirect("contact_us")
    else:
        if request.user.is_authenticated:
            try:
                profile_email = UserProfile.objects.get(user=request.user)
                form = ContactForm(initial={"email": profile_email.user.email})
            except UserProfile.DoesNotExist:
                form = ContactForm()
        else:
            form = ContactForm()

    template = "connect/contact.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
