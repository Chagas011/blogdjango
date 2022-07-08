
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        help_text=(
            'Coloque seu Username aqui'
        ),
        error_messages={
            'required': 'Este campo é obrigatorio',
            'min_length': 'Username precisa ter mais que 4 caracteres',
            'max_length': 'Username precisa ter menos que 150 caracteres',
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        error_messages={'required': 'Digite seu primeiro nome aqui'},
        label='Primeiro nome'
    )
    last_name = forms.CharField(
        error_messages={'required': 'Digite seu ultimo nome aqui'},
        label='Ultimo nome'
    )
    email = forms.EmailField(
        error_messages={'required': 'E-mail é obrigatorio'},
        label='E-mail',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'A senha nao pode estar vazia'
        },
        help_text=(
            'A senha deve ter pelo menos uma letra minuscula'
            'uma maiuscula e um numero. O comprimeto da senha '
            'deve ter pelo menos 8 caracteres'
        ),
        validators=[strong_password],
        label='Senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirme sua senha',
        error_messages={
            'required': 'Repita sua senha'
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
