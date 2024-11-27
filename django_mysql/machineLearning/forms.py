from django import forms
from .models import Respuesta

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['pregunta1', 'pregunta2', 'pregunta3', 'pregunta4',
                  'pregunta5', 'pregunta6', 'pregunta7', 'pregunta8']


