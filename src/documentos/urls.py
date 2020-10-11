from django.urls import path
from .views import DocumentoList

documentos_patterns = ([
    path('', DocumentoList.as_view(), name='documentos'),
], 'documentos')
