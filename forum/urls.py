
from django.urls import include, path, re_path
from forum import views

app_name = 'forum'
urlpatterns = [
    re_path(r'(?P<pk>[0-9]+)$', views.detail, name='detail'),
    re_path(r'^/?$', views.list, name='list'),
]
