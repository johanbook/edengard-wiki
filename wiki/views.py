from django.shortcuts import render

from .models import Article


def about(request):
    return render(request, 'wiki/about.html')


def home(request):
    context = {
        'article': Article.objects.first()
    }
    return render(request, 'wiki/home.html', context)



