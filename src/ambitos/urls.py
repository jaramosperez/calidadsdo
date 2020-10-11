from django.urls import path
from .views import AmbitoList, AmbitoDetail

ambitos_patterns = ([
    path('', AmbitoList.as_view(), name='ambitos'),
    path('<int:pk>/<slug:slug>/', AmbitoDetail.as_view(), name='ambito'),
], 'ambitos')