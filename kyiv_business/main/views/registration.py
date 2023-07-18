from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View
from ..forms import NewUserForm


class RegistrationView(View):
    @staticmethod
    def get(request):
        form = NewUserForm()
        return render(request, "registration.html", {"form": form})

    @staticmethod
    def post(request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            if "email" in form.errors:
                messages.error(request, "Invalid email address")
            if "username" in form.errors:
                messages.error(request, "Invalid username")
            if "password1" in form.errors:
                messages.error(request, "Invalid password")
            if "password2" in form.errors:
                messages.error(request, "Passwords do not match")

        return render(request, "registration.html", {"form": form})
