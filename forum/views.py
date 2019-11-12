from django.shortcuts import render
from forum import models

def list(request):
    articles = models.Article.objects.order_by('-id')[:10]
    print (articles)
    context = {
        'articles': articles,
    }
    return render(request, 'list.html', context)

def detail(request, pk):
    article = models.Article.objects.get(pk=pk)
    print (article.subject)

    prev_articles = models.Article.objects \
        .filter(id__lt=article.id) \
        .order_by('-id')[:2][::-1]

    next_articles = models.Article.objects \
        .filter(id__gt=article.id) \
        .order_by('id')[:2]

    context = {
        'article': article,
        'prev_articles': prev_articles,
        'next_articles': next_articles
    }
    return render(request, 'view.html', context)
