from django.db .models import TextField
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from . import models


def about(request):
    return render(request, "wiki/about.html")


def home(request):
    return render(request, "wiki/home.html")


def get_category_view(category_model):
    class CategoryListView(ListView):
        model = category_model
        template_name = 'wiki/category.html'

        def get_context_data(self, **kwargs):
            context = super(CategoryListView, self).get_context_data(**kwargs)
            context['category'] = self.model.__name__
            context['article_url'] = f'wiki-{self.model.__name__.lower()}-article'
            return context
    return CategoryListView.as_view()


def article_by_model(model):
    def view_article(request, title):
        article = model.objects.filter(title__iexact=title).first()
        if article:
            return render(
                request,
                "wiki/article.html",
                context={
                    'article': article,
                    'fields': [field for field in article._meta.fields if isinstance(field, TextField)]
                }
            )
        else:
            raise Http404
    return view_article


class SearchResultsView(ListView):
    template_name = 'wiki/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        found = []
        for model in models.MODELS:
            found.extend(self.query_by_model(query, model))
        return found

    @staticmethod
    def query_by_model(query, model):
        return model.objects.filter(
            keywords__icontains=query
        )
