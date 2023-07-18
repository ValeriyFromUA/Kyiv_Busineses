import re

from django.views.generic import ListView
from ..models import Activity


class CategoriesView(ListView):
    template_name = "categories.html"
    model = Activity
    paginate_by = 100
    context_object_name = "categories"
    ordering = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        filtered_queryset = []

        for activity in queryset:
            name = activity.name
            if not re.search(r'[а-яіїєґ][А-ЯІЇЄҐ]', name):
                filtered_queryset.append(activity)

        return filtered_queryset
