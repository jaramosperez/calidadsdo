from .models import Documento
from django.urls import reverse_lazy
from .forms import DocumentoForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(), name='dispatch')
class DocumentoList(ListView):
    """
    Clase para listar todos los documentos.
    """
    model = Documento


@method_decorator(login_required(), name='dispatch')
class DocumentoCreate(CreateView):
    """
    Clase para ingresar documentos al sistema.
    No Tiene Filtro de Archivos
    [TODO]
    Crear un filtro para tipo de archivos.
    """
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos:documentos')
