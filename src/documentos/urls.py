from django.urls import path
from .views import DocumentoList, DocumentoCreate

documentos_patterns = ([
    path('', DocumentoList.as_view(), name='documentos'),
    path('crear/', DocumentoCreate.as_view(), name="crear"),
], 'documentos')
