from django.db import models
from django.utils import timezone

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, null=True)
    #fecha en la que es guardada la noticia
    date = models.DateTimeField(default=timezone.now)
    redactor = models.CharField(max_length=200, default='Tomás Salgado')
    #False = foto/s no este en la galeria, True = foto/s aparezca en la galeria
    galeria = models.BooleanField(default=False, blank=True, null=True)
    tema = models.CharField(max_length=100, null=True, blank=True)


#modelo que contiene foto relacionada a una noticia 
class Images(models.Model):
    #clave foranea de una Noticia
    noticia = models.ForeignKey(Noticia,on_delete=models.CASCADE)
    #imagen que guardamos en la carpeta noticias
    image = models.ImageField(upload_to='fotos',null=True,blank=True)