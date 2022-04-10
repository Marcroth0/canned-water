from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestProfileViews(TestCase):
    """ Test profiles views """

    def setUp(self):
        """ Set up test data """
        self.client = Client()
        self.test_user = User.objects.create_user(
                        username='mike',
                        email="mike@email.com",
                        password='test123')

    def test_url_response(self):
        """ Test URL response success """
        login = self.client.login(username='mike',
                                  password='test123')
        response = self.client.get('/profile/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """ Test URL is accessible """
        login = self.client.login(username='mike',
                                  password='test123')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        login = self.client.login(username='mike',
                                  password='test123')
        response = self.client.get(reverse('profile'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertTemplateNotUsed(response, 'bag/bag.html')
        
    