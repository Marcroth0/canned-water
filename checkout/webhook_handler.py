from django.http import HttpResponse

class StripeWH_Handler:

    def __init__(self, request):
        """Handle Stripe webhooks"""
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received:{event["type"]}',
            status=200
        )
