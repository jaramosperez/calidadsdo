from .models import Caracteristica
from .forms import CaracteristicaFormUpdate
from documentos.models import Documento
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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


@method_decorator(login_required(), name='dispatch')
class CaracteristicaUpdate(UpdateView):
    model = Caracteristica
    form_class = CaracteristicaFormUpdate
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('caracteristicas:caracteristica')
