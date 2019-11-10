from django.shortcuts import render
from forum import models

def index(request):
    return render(request, 'view.html')
