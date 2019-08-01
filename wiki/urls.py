from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="wiki-home"),
    path("about/", views.about, name="wiki-about"),
    path("search/", views.SearchResultsView.as_view(), name="search"),
]
