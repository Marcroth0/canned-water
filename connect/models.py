from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=70, null=False, blank=False)
    title = models.CharField(max_length=40, null=False, blank=False)
    content = models.TextField(max_length=900, null=False, blank=False)

    def __str__(self):
        return self.title


