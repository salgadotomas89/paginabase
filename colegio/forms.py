from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from colegio.models import AppearanceSettings, Colegio, Evento, Menu, MenuItem


class AppearanceSettingsForm(forms.ModelForm):
    menu_background_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    menu_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    mega_menu_background_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    mega_menu_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    menu_height = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 50, 'max': 200}))
    color_principal_texto= forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = AppearanceSettings
        fields = ['menu_background_color', 'menu_text_color', 'mega_menu_background_color', 'mega_menu_text_color', 'menu_height', 'color_principal_texto']


class CustomUserForm(UserCreationForm):
    ROLES_CHOICES = [
        ('', 'Seleccione un rol'),
        ('profesor', 'Profesor'),
        ('utp', 'UTP'),
        ('director', 'Director')
    ]

    username = forms.CharField(label='Nombre de usuario')
    first_name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLES_CHOICES, label='Rol', required=False)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', 'role')

class FormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class FormColegio(forms.ModelForm):

    class Meta:
        model = Colegio
        fields = '__all__'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'url']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_items']
        widgets = {
            'menu_items': forms.CheckboxSelectMultiple,
        }