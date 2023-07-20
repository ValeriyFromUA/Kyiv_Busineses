from django.db.models import Q
from django.views.generic import TemplateView
from django.shortcuts import render

from main.models import Company


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        search_name = request.POST.get('search_name', '')

        companies = Company.objects.filter(
            Q(name__icontains=search_name.lower()) | Q(name__icontains=search_name.upper()))

        context = {
            'companies': companies,
            'search_name': search_name,
        }
        return render(request, self.template_name, context)
