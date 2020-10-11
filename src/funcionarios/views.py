from .models import Funcionario
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(), name='dispatch')
class FuncionarioList(ListView):
    model = Funcionario


@method_decorator(login_required(), name='dispatch')
class FuncionarioDetail(DetailView):
    model = Funcionario

    def get_context_data(self, **kwargs):
        context = super(FuncionarioDetail, self).get_context_data(**kwargs)
        funcionario_listado = Funcionario.objects.filter(
            funcionario_id=self.object.id
            )
        context['funcionario_listado'] = funcionario_listado

        return context
