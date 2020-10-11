from django.urls import path
from .views import CaracteristicaList, CaracteristicaDetail
from .views import CaracteristicaUpdate

caracteristicas_patterns = ([
    path('', CaracteristicaList.as_view(), name='caracteristicas'),
    path(
        '<int:pk>/<slug:slug>/',
        CaracteristicaDetail.as_view(),
        name='caracteristica'),
    path(
        'actualizar/<int:pk>/<slug:slug>/',
        CaracteristicaUpdate.as_view(), name='actualizar'
        ),
], 'caracteristicas')
