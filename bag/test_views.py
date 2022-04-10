from django.test import TestCase, Client
from django.urls import reverse

from products.models import Product
from django.contrib.messages import get_messages

class TestBagViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_page = reverse("home")
        self.view_bag = reverse("view_bag")
        self.item = Product.objects.create(name="test-item", price="1")
        self.add_to_bag = reverse("add_to_bag",
                                   kwargs={"item_id": self.item.id})
        self.adjust_bag = reverse("adjust_bag",
                                   kwargs={"item_id": self.item.id})
        self.remove_from_bag = reverse("remove_from_bag",
                                        kwargs={"item_id": self.item.id})

    def test_add_product_to_bag(self):
        """
        Test that product gets added to bag and that more products are addable
        """

        response = self.client.post(self.add_to_bag,
                                    data={"quantity": "1",
                                          "redirect_url": "/"})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Added {self.item.name} to your bag')

        response = self.client.post(self.view_bag)
        context = response.context
        self.assertEqual(context["bag_items"][0]["item_id"],
                         f"{self.item.id}")

        response = self.client.post(self.add_to_bag,
                                    data={"quantity": 3,
                                          "redirect_url": "/"})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Updated {self.item.name} quantity to 4')


    def test_view_bag(self):
        response = self.client.get(self.view_bag)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")

    def test_adjust_bag(self):
        response = self.client.post(self.adjust_bag,
                                    data={"quantity": 2})
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Updated {self.item.name} quantity to 2')

        response = self.client.post(self.view_bag)
        context = response.context
        self.assertEqual(context["bag_items"][0]["quantity"], 2)

    def test_remove_from_bag(self):
        self.client.post(self.add_to_bag, data={"quantity": "2"})

        response = self.client.post(self.remove_from_bag)
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         f'Removed {self.item.name} from your bag')



