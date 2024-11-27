
from django import forms

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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        help_text="Introduce un correo electrónico válido."
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']