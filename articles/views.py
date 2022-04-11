from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import ArticlePostForm, CommentForm

def view_articles(request):
    """View to return all articles """

    blogs = Post.objects.all().order_by('-date_published')

    context = {
        'blogs': blogs,
    }
    
    return render(request, "articles/articles.html", context)

def article_details(request, post_id):
    comments = Comment.objects.filter(post=post_id).order_by('-date_published')
    form = CommentForm()
    blog_post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': blog_post,
        'comments': comments,
        'comment_form': form,
    }

    return render(request, "articles/article_post_detail.html", context)

@login_required
def add_article_post(request):

    if request.user.is_superuser:
        if request.method == "POST":
            form = ArticlePostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "Article uploaded!")
                return redirect(reverse("article_details", args=[post.id]))

            else:
                messages.error(request,
                               "Sorry! Didn't work")
        else:
            form = ArticlePostForm()
    else:
        messages.error(request, 'Sorry, but you are no Admin')

    template = "articles/add_article_post.html"

    context = {
        "form": form,
    }
    return render(request,
                  template,
                  context,)

def delete_article_post(request, post_id):

    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        messages.info(request, "It's gone!")
    else: 
        messages.error(request, "Sorry, not in this world.")
    
    return redirect(reverse('view_articles'))

def edit_article_post(request, post_id):

    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
        if request.method == "POST":
            form = ArticlePostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 "Done! Post updated!")
                return redirect(reverse("article_details", args=[post.id]))
        else:
            form = ArticlePostForm(instance=post)
    else:
        messages.error(request, 'Nah, does not work like that')
        return redirect(reverse("view_articles"))

    context = {
        "form": form,
        "post": post,
    }

    return render(request,
                  "articles/edit_article_post.html",
                  context)
