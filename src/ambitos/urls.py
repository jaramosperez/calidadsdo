from django.urls import path
from .views import AmbitoList, AmbitoDetail, AmbitoUpdate

"""
Listado de endpoints(URL) relaciondas a los ámbitos.
"""
ambitos_patterns = ([
    path('', AmbitoList.as_view(), name='ambitos'),
    path('<int:pk>/<slug:slug>/', AmbitoDetail.as_view(), name='ambito'),
    path(
        'actualizar/<int:pk>/<slug:slug>/',
        AmbitoUpdate.as_view(), name='actualizar'
        ),
], 'ambitos')
