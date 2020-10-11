from django.contrib import admin
from .models import Documento, TipoDocumento


class DocumentoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('tipo_documento', 'caracteristica', 'vigencia')
    readonly_fields = ('created', 'updated')


class TipoDocumentoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('nombre',)


admin.site.register(Documento, DocumentoAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
