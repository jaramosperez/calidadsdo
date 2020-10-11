from django.contrib import admin
from .models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('nombres', 'primer_apellido')
    readonly_fields = ('created', 'updated')


admin.site.register(Funcionario, FuncionarioAdmin)
