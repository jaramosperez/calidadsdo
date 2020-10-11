from .models import Documento
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(), name='dispatch')
class DocumentoList(ListView):
    model = Documento
