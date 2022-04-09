from django.shortcuts import render

def contact_us(request):
    """View to let users send email to owner of site """

    template = "connect/contact.html"
    
    return render(request, template)
