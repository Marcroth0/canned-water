from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from products.models import Product, Category


class TestProductsViews(TestCase):
    """Test Product views for all types of user"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_user',
            email='test@test.com',
            password='testpassword'
        )
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category"
        )
        self.product = Product.objects.create(
            sku="123",
            name="test product",
            description="test description",
            price=1200,
            image="testimg.jpg",
            category=self.category,
        )
        self.all_products = reverse("products")
        self.product_detail = reverse("product_detail",
                                      kwargs={"product_id": self.product.id})

        # Views with superuser restrictions

        self.super_user = User.objects.create_superuser(
            username='test_admin',
            email='testadmin@test.com',
            password='testadminpassword'
        )

        self.add_product = reverse("add_product")
        self.home = reverse("home")
        self.edit_product = reverse("edit_product",
                                    kwargs={"product_id": self.product.id})
        self.delete_product = reverse("delete_product",
                                      kwargs={"product_id": self.product.id})

    def test_all_products_view(self):
        """
        Test the all products view
        """

        response = self.client.get(self.all_products)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertTemplateUsed(response, "base.html")

    def test_all_products_views_with_search(self):
        """
        Test the all_products view with a search query parameter
        """

        response = self.client.get(self.all_products,
                                   {"q": "test"})
        context = response.context
        self.assertTrue(context['search_term'])
        self.assertEqual(context['search_term'], 'test')

    def test_view_product_detail_view(self):
        """ Test the product_detail view """

        response = self.client.get(self.product_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")


    def test_view_product_detail_view(self):
        """ Test the product_detail view """

        response = self.client.get(self.product_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        
    # Views with user/superuser restrictions

    def test_add_product_not_superuser(self):
        """ Test the add_product view if the user is not a superuser """

        self.client.login(
            username="test_user", password="testpassword")
        response = self.client.get(self.add_product)
        self.assertRedirects(response, self.home)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, you are not a superuser.')

    def test_add_product_superuser_GET(self):
        """ Test the add_product GET functionality for superusers """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.get(self.add_product)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")
        self.assertTemplateUsed(response, "base.html")

    def test_add_product_invalidform_POST(self):
        """ Test the add_product view using an invalid form """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.add_product, {
            "category": self.category,
            "sku": "",
            "name": "",
            "description": "",
            "price": "",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Failed to add product. Please ensure the form is valid.')

    def test_add_product_validform_POST(self):
        """ Test the add_product view with a valid form """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.add_product, {
            "name": "Test product",
            "description": "test description",
            "price": 1200,
        })
        product = Product.objects.get(name="Test product")
        self.assertTrue(product)
        self.assertEqual(product.description, "test description")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Successfully added product!')

    def test_edit_product_not_superuser(self):
        """ Test the edit_product view if the user is not a superuser """

        self.client.login(
            username="test_user", password="testpassword")
        response = self.client.get(self.edit_product)
        self.assertRedirects(response, self.home)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, you are not a superuser.')

    def test_edit_product_superuser_GET(self):
        """ Test the edit_product GET functionality if superuser """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.get(self.edit_product)
        self.assertEqual(response.context['form'].initial['name'],
                         self.product.name)
        self.assertEqual(response.context['form'].initial['description'],
                         self.product.description)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")
        self.assertTemplateUsed(response, "base.html")

    def test_edit_product_invalidform_POST(self):
        """ Test the edit_product view post with an invalid form"""

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.edit_product, {
            "name": "",
            "description": "",
            "price": "",
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Failed to update product.\
 Please check the form is valid.')

    def test_edit_product_validform_POST(self):
        """ Test edit_product view with a valid form """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.post(self.edit_product, {
            "name": "Test edited product",
            "description": "test edited description",
            "price": 1300,
        }
        )
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.description, 'test edited description')
        self.assertEqual(product.price, 1300)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Successfully updated item!')

    def test_delete_product_not_superuser(self):
        """ Test delete_product view if user is not superuser """

        self.client.login(
            username="test_user", password="testpassword")
        response = self.client.get(self.delete_product)
        self.assertRedirects(response, self.home)
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, you are not a superuser.')

    def test_delete_product_superuser_GET(self):
        """ Test delete_product view GET functionality if a superuser """

        self.client.login(
            username="test_admin", password="testadminpassword")
        response = self.client.get(self.delete_product)
        self.assertRedirects(response, self.all_products)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Product deleted!')
