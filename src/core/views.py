from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    """
    Clase que carga la página inicial del sistema.
    """
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name, {'title': 'Calidad Sol de oriente'}
            )
