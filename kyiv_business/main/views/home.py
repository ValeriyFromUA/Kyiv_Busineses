from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, "home.html")
