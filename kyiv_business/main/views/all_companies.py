from django.shortcuts import render
from django.views.generic import ListView
from ..models import Company


class CompaniesView(ListView):
    template_name = "companies.html"
    model = Company
    context_object_name = "companies"
    paginate_by = 100
    ordering = ["name"]
