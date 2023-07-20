from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from ..models import Company, Activity


class ActivityView(ListView):
    template_name = "companies.html"
    context_object_name = "companies"
    paginate_by = 100

    def get_queryset(self):
        activity_pk = self.kwargs['pk']
        activity = get_object_or_404(Activity, pk=activity_pk)
        companies = activity.companies.all()
        return companies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_pk = self.kwargs['pk']
        activity = get_object_or_404(Activity, pk=activity_pk)
        context['category_name'] = activity.name
        return context
