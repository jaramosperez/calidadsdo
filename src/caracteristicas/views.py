from .models import Caracteristica
from documentos.models import Documento
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required(), name='dispatch')
class CaracteristicaList(ListView):
    model = Caracteristica


@method_decorator(login_required(), name='dispatch')
class CaracteristicaDetail(DetailView):
    model = Caracteristica

    def get_context_data(self, **kwargs):
        context = super(CaracteristicaDetail, self).get_context_data(**kwargs)
        documento_listado = Documento.objects.filter(
            caracteristica_id=self.object.id
            )
        context['documento_listado'] = documento_listado

        return context
