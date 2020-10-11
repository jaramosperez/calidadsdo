from django.urls import path
from .views import CaracteristicaList, CaracteristicaDetail

caracteristicas_patterns = ([
    path('', CaracteristicaList.as_view(), name='caracteristicas'),
    path('<int:pk>/<slug:slug>/', CaracteristicaDetail.as_view(), name='caracteristica'),
], 'caracteristicas')