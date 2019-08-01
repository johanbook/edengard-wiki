from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AccountRegistrationForm


def register(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, "Account request sent")
            return redirect("wiki-home")
    else:
        form = AccountRegistrationForm()
    return render(request, "users/register.html", {"form": form})
