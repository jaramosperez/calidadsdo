from django.contrib import admin
from .models import Caracteristica


# Register your models here.
class CaracteristicaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('nombre', 'ambito')
    readonly_fields = ('created', 'updated')


admin.site.register(Caracteristica, CaracteristicaAdmin)
