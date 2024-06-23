from django.db import models

# Create your models here.


class Book(models.Model):
    nombre = models.TextField()
    tema = models.TextField(default='')
    autor = models.TextField()
    isbn = models.TextField()
    editorial = models.TextField()
    resumen = models.TextField(blank=True)
    foto = models.ImageField(upload_to='libros', blank=True)
    cantidad = models.IntegerField(default=1, blank=True, null=True)
    anio = models.TextField(default='2000')
    edad = models.TextField(default='confirmar rango')

    def __str__(self):
        return self.nombre