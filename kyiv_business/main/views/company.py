from django.views.generic import DetailView

from main.models import Company


class CompanyView(DetailView):
    model = Company
    template_name = "company.html"
    context_object_name = "company"

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Company.objects.get(pk=pk)
