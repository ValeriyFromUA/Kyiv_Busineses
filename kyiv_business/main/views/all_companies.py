from django.shortcuts import render
from django.views.generic import ListView
from ..models import Client


class CompaniesView(ListView):
    template_name = "companies.html"
    model = Client
    context_object_name = "companies"
    paginate_by = 100
    ordering = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get("order_by")
        if order_by and order_by in [field.name for field in Client._meta.get_fields()]:
            queryset = queryset.order_by(order_by)

        # Оновлення полів, видаляючи фігурні дужки
        model_fields = Client._meta.get_fields()
        for obj in queryset:
            for field in model_fields:
                if field.name != 'id':
                    field_value = getattr(obj, field.name)
                    if field_value and isinstance(field_value, str):
                        setattr(obj, field.name, field_value.replace("{", "").replace("}", ""))

        return queryset
