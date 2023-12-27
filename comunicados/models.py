from django.utils import timezone
from django.db import models

# Create your models here.
class Comunicados(models.Model):
    title = models.CharField(max_length=50, default='Comunicados')
    background = models.CharField(max_length=100, default="rgba(132, 158, 214, 0.65)")
    image = models.ImageField(upload_to='comunicados',null=True,blank=True)

class Comunicado(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100, default='Mauricio Orellana', null=True, blank=True)
    texto = models.TextField(max_length=1000)
    fecha = models.DateTimeField(default=timezone.now)

class ArchivosComunicado(models.Model):
    comunicado = models.ForeignKey(Comunicado,on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='comunicados',null=True,blank=True)