from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import ArticlePostForm

def view_articles(request):
    """View to return all articles """

    blogs = Post.objects.all().order_by('-date_published')

    template = "articles.html"
    context = {
        'blogs': blogs,
    }
    
    return render(request, template, context)

def article_details(request, article_id):

    article = get_object_or_404(Post, pk=article_id)
    template = "articles/article_post_detail.html"

    context = {
        'article': article,
    }

    return render(request, template, context)

@login_required
def add_article_post(request):

    if request.user.is_superuser:
        if request.method == "POST":
            form = ArticlePostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
            else:
                messages.error(request,
                               "Sorry! Didn't work")
        else:
            form = ArticlePostForm()
    else:
        messages.error(request, 'Sorry, but you are no Admin')

    template = "add_article_post.html"

    context = {
        "form": form,
    }
    return render(request,
                  template,
                  context,)
