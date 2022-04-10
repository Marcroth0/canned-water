from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import Post

class TestArticleViews(TestCase):

    def SetUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='mark',
            email='mark@email.com',
            password='test123'
        )
        self.post = Post.objects.create(
            title="test",
            author=self.admin,
            content="Test Description",
            description="Test Description"
        )

        
