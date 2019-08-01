from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


def about(request):
    return render(request, 'wiki/about.html')


def home(request):
    context = {
        'article': Article.objects.first()
    }
    return render(request, 'wiki/home.html', context)


def search(request, keywords):
    print(keywords)
    return render(request, 'wiki/home.html', context=None)


class SearchResultsView(ListView):
    model = Article
    template_name = 'wiki/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        return Article.objects.filter(
            content__icontains=query
        )
