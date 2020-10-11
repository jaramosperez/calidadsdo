from django import forms
from .models import Ambito


class AmbitoFormUpdate(forms.ModelForm):
    class Meta:
        model = Ambito
        fields = ['funcionario']
        widgets = {
            'funcionario': forms.Select(
                attrs={'class': 'ui selection dropdown'}
                ),
        }
