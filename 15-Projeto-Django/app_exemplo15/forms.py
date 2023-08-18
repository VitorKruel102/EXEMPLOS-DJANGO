from django import forms
from django.core.exceptions import ValidationError

class ContatoForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs['placeholder'] = 'Digite o seu  nome.'

    nome = forms.CharField(
        label='Nome',
        help_text=('Lembre-se de colocar apenas o primeiro nome.'),
        error_messages={
            'required': 'Esse campo não pode ser nulo',
            'min_length': 'Mínimo de 3 letras',
            'max_length': 'Máximo de 25 letras',
        },
        max_length=25,
        min_length=3
    )

    email = forms.EmailField(
        label='E-mail',
        help_text='O e-mail deve ser válido',
        error_messages={
            'required': 'Esse campo não pode ser nulo.'
        }
    )

    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Esse campo não pode ser nulo',
        },
        help_text='Esse campo deve conter: Letras minusculas e maiusculas, assim como números.',
    )

    senha_confirmacao = forms.CharField(
        label='Confirmar Senha',
        widget= forms.PasswordInput(),
        error_messages={
            'required': 'Esse campo não pode ser nulo',
        },
        help_text='Esse campo deve conter: Letras minusculas e maiusculas, assim como números.',
    )
    
    def clean(self):
        cleaned_data = super().clean()

        password = self.cleaned_data.get('senha')
        password2 = self.cleaned_data.get('senha_confirmacao')

        if password != password2:
            raise ValidationError({
                'senha': ValidationError(
                    'Senha são diferentes',
                    code='invalid'
                ),
                'senha_confirmacao': 'Senha são diferentes',
            }
            )

