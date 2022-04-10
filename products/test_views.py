from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class TestProductsViews(TestCase):
    """ Test the products response  """

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTemplateNotUsed(response, 'bag/bag.html')


# class TestIndividualProductViews(TestCase):

#     def setUp(self):
#         """ Set up test data """
#         self.client = Client()
#         self.product = Product.objects.create(pk=1,
#                                               name="testproduct",
#                                               price=40.00)

#     def test_view_uses_correct_template(self):
#         response = self.client.get(f'/products/{self.product.id}/')
#         self.assertTemplateUsed(response, 'products/product_detail.html')
