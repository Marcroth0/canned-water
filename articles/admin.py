from django.contrib import admin
from .models import Post


class ArticlePostAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'author',
                    'date_published',
                    'featured_articles',)

    list_editable = ('featured_articles',)

    ordering = ('-date_published', )


admin.site.register(Post, ArticlePostAdmin)
