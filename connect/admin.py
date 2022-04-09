from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'content',
                    'email',)


admin.site.register(Contact, ContactAdmin)
