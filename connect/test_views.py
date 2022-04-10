from django.test import TestCase, Client
from django.urls import reverse


class TestContactViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url(self):
        """ Test URL response success """
        response = self.client.get('/connect/')
        self.assertEqual(response.status_code, 200)


    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('contact_us'))
        self.assertTemplateUsed(response, 'connect/contact.html')
        self.assertTemplateNotUsed(response, 'bag/bag.html')

    # def test_can_send_contact_form(self):
    #     """
    #     Check if the form get submit
    #     and redirects back to contact page
    #     """
    #     response = self.client.post('/contact_us/', {'email': 'test@mail.com',
    #                                               'title': 'title',
    #                                               'content': 'test'})
    #     self.assertEqual(response.status_code, 200)

