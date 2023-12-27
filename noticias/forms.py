from django import forms

from noticias.models import Noticia


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "subtitulo","texto","redactor", "galeria"]

class FormImagesNoticias(FormNoticia): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(FormNoticia.Meta):
        fields = FormNoticia.Meta.fields + ['images',]