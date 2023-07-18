from django.shortcuts import render
from django.views.generic import ListView
from ..models import Client


class ActivityView(ListView):
    template_name = "activity_companies.html"
    model = Client
    context_object_name = "companies"
    paginate_by = 100

    def get_queryset(self):
        activity = self.kwargs.get('activity')
        queryset = Client.objects.filter(activity__icontains=activity)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity = self.kwargs.get('activity')
        context['searched_activity'] = activity
        return context
