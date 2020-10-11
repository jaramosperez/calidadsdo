from django import forms
from .models import Caracteristica


class CaracteristicaFormUpdate(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ['funcionario']
        widgets = {
            'funcionario': forms.Select(
                attrs={'class': 'ui selection dropdown'}
                ),
        }
