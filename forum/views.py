
from django.conf import settings
from django.shortcuts import render, render_to_response
from forum import models

def sitemap(request):
    articles = models.Article.objects.order_by('-id')[:500]
    context = {
        'articles': articles,
    }
    response = render(request, 'sitemap.xml', context)
    response['Content-Type'] = 'application/xml;'
    return response

def rss(request):
    articles = models.Article.objects.order_by('-id')[:100]
    context = {
        'articles': articles,
    }
    response = render(request, 'rss.xml', context)
    response['Content-Type'] = 'application/xml;'
    return response

def robots(request):
    response = render(request, 'robots.txt', {})
    response['Content-Type'] = 'text/plain;'
    return response

def list(request):
    articles = models.Article.objects.order_by('-id')[:20]
    context = {
        'brand': settings.BRAND,
        'title': settings.TITLE,
        'description': settings.DESCRIPTION,
        'articles': articles,
    }
    return render(request, 'list.html', context)

def detail(request, pk):
    article = models.Article.objects.get(pk=pk)

    prev_articles = models.Article.objects \
        .filter(id__lt=article.id) \
        .order_by('-id')[:2][::-1]

    next_articles = models.Article.objects \
        .filter(id__gt=article.id) \
        .order_by('id')[:2]

    context = {
        'title': article.subject,
        'description': article.description,
        'article': article,
        'prev_articles': prev_articles,
        'next_articles': next_articles
    }
    return render(request, 'view.html', context)
