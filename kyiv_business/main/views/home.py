from django.views.generic import TemplateView
from django.shortcuts import render

from main.models import Company, Activity


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        search_name = request.POST.get('search_name', '')
        search_activity = request.POST.get('search_activity', '')

        companies = Company.objects.all()
        activities = Activity.objects.all()

        if search_name:
            companies = companies.filter(name__icontains=search_name)

        context = {
            'companies': companies,
            'search_name': search_name,
        }
        return render(request, self.template_name, context)
