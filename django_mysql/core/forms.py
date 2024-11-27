
from django import forms
from .models import Respuesta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['pregunta1', 'pregunta2', 'pregunta3', 'pregunta4']
