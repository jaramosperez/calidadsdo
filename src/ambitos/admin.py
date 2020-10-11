from django.contrib import admin
from .models import Ambito


class AmbitoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero')


admin.site.register(Ambito, AmbitoAdmin)