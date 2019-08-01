from django.urls import path
from . import views
from .models import MODELS

urlpatterns = [
    path("", views.home, name="wiki-home"),
    path("about/", views.about, name="wiki-about"),
    path("search/", views.SearchResultsView.as_view(), name="search"),
]

for model in MODELS:
    name = model.__name__.lower()
    urlpatterns.append(
        path(f'{name}/', views.get_category_view(model), name=f'wiki-{name}')
    )
