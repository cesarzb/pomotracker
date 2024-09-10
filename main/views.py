from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
    print("Home view called")
    return render(request, "main/home.html", {})


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "registration/sign_up.html", {"form": form})
