from django.contrib import admin
from .models import Ambito


class AmbitoAdmin(admin.ModelAdmin):
    """
    Clase para usar el Modelo Ambito en el DjangoAdmin.
    """
    list_display = ('nombre', 'numero')


admin.site.register(Ambito, AmbitoAdmin)
