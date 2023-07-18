from django.views.generic import ListView
from ..models import Client
from itertools import chain
import re
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.fields import JSONField
from django.db.models import F

from ..utils import get_distinct_activities


class CategoriesView(ListView):
    template_name = "categories.html"
    model = Client
    paginate_by = 100

    def get_queryset(self):
        return Client.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_distinct_activities()
        return context
