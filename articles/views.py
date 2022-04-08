from django.shortcuts import render

def view_articles(request):
    """View to return articles """
    template = "article/articles.html"
    
    return render(request, template)
