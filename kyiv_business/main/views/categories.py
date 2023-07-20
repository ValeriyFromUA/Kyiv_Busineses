import re
from django.views.generic import ListView
from ..models import Activity


class CategoriesView(ListView):
    template_name = "categories.html"
    model = Activity
    paginate_by = 400
    context_object_name = "categories"
    ordering = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if search_query:
            # Фільтруємо результати, якщо переданий параметр search
            filtered_queryset = []
            for activity in queryset:
                name = activity.name
                if re.search(search_query, name, re.IGNORECASE):
                    filtered_queryset.append(activity)
            return filtered_queryset
        else:
            return queryset
