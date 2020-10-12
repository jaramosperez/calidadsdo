from .models import Ambito
from caracteristicas.models import Caracteristica
from .forms import AmbitoFormUpdate
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(), name='dispatch')
class AmbitoList(ListView):
    """ Clase para listar todos los ámbitos. """
    model = Ambito


@method_decorator(login_required(), name='dispatch')
class AmbitoDetail(DetailView):
    """ Clase para mostrar el detalle del ámbito y sus caraceristicas. """
    model = Ambito

    def get_context_data(self, **kwargs):
        """ Función para mostrar listado de características del ámbito. """
        context = super(AmbitoDetail, self).get_context_data(**kwargs)
        caracteristica_listado = Caracteristica.objects.filter(
            ambito_id=self.object.id
            )
        context['caracteristica_listado'] = caracteristica_listado

        return context


@method_decorator(login_required(), name='dispatch')
class AmbitoUpdate(UpdateView):
    """ Clase para modificar el encargado de ámbito. """
    model = Ambito
    form_class = AmbitoFormUpdate
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ambitos:ambitos')
