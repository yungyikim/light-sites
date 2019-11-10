
from django.urls import include, path
from forum import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
]
