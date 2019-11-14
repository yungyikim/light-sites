"""sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forum import views

urlpatterns = [
    path('sitemap.xml', views.sitemap, name="sitemap_xml"),
    path('rss', views.rss, name="rss"),
    path('robots.txt', views.robots, name="robots"),
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path(r'', views.list, name='home'),
]
