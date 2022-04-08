from django import forms
from .models import Post

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            "image",
            "body",
            "description",
            "title",
        }

    field_order = ['title', 'description','body', 'image']

    image = forms.ImageField(
        label="Image",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

