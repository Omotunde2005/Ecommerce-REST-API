from django.shortcuts import render, redirect
from products_app import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from products_app import models
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token


# Create your views here.
def home_view(request):
    context = {
        "title": "Home"
    }
    return render(request, "index.html", context=context)


def register_view(request):
    form = forms.RegistrationForm()
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect("home")

        else:
            messages.error(request, "An error occurred during registration")
            return redirect("register")

    context = {
        "form": form
    }
    return render(request, "signup_page.html", context=context)


def login_view(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                models.User.objects.get(email=email)

            except models.User.DoesNotExist:
                messages.error(request, "Email does not exist")
                return redirect("login")
            else:
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.error(request, "Incorrect password.")

        else:
            messages.error(request, "An error occurred during login")
            return redirect("login")

    context = {
        "form": form
    }
    return render(request, "login_page.html", context=context)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url="/login")
def dashboard(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    context = {
        "token": token
    }
    return render(request, "dashboard.html", context=context)


@login_required(login_url="/login")
def generate_access_token(request, identifier):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return redirect("dashboard", identifier=identifier)