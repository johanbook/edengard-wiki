from django.shortcuts import render


def about(request):
    return render(request, 'wiki/about.html')


def home(request):
    return render(request, 'wiki/home.html')



