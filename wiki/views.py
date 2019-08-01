from django.shortcuts import render
from django.views.generic import ListView

from . import models


def about(request):
    return render(request, "wiki/about.html")


def home(request):
    return render(request, "wiki/home.html")


def category(request):
    print(request)
    context = {"article": None}  # Article.objects.first()
    return render(request, "wiki/home.html", context)


def get_category_view(category_model):
    class CategoryListView(ListView):
        model = category_model
        template_name = 'wiki/category.html'

        def get_context_data(self, **kwargs):
            context = super(CategoryListView, self).get_context_data(**kwargs)
            context['category'] = self.model.__name__
            return context
    return CategoryListView.as_view()


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
