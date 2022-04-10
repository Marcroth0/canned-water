from django.test import TestCase, Client
from django.urls import reverse


class TestCacheCheckoutViews(TestCase):
    """ Check chace checkout data works """

    def setUp(self):
        self.client = Client()

    def test_cache_data(self):
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)


class TestCheckoutViews(TestCase):
    """ Check checkout view  """

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test response success """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        self.assertTemplateNotUsed(response, "bag/bag.html")

    