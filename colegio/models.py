from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
#blank=True quiere decir que el campo no es obligatorio en el formulario
#null=True es para que la base de datos sepa que puede dejar ese campo vacio

#el modelo comunicados hace referencia a la seccion comunicados que tiene un titulo, color de fondo e imagen
DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

class AppearanceSettings(models.Model):
    #color de fondo del menu principal
    menu_background_color = models.CharField(max_length=7, default="#FFFFFF")
    #color del texto
    menu_text_color = models.CharField(max_length=7, default="#000000")
    #tamaño
    menu_height = models.PositiveIntegerField(default=80, validators=[MinValueValidator(50), MaxValueValidator(200)])

    #color de fondo del megamenu
    mega_menu_background_color = models.CharField(max_length=7, default="#FFFFFF")
    #color del texto del megamenu
    mega_menu_text_color = models.CharField(max_length=7, default="#000000")

    #color cuando paso por encima de un texto especial
    color_principal_texto = models.CharField(max_length=7, default="#000000")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('profesor', 'Profesor'), ('utp', 'UTP'), ('director', 'Director')])
    jefe = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    asignaturas = models.ManyToManyField(Asignatura, through='CursoAsignatura', blank=True, null=True)
    profesor_jefe = models.ForeignKey(UserProfile, related_name='curso_profesor_jefe', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class CursoAsignatura(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.asignatura.nombre

class Evento(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

class Colegio(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='fotos', blank=True, null=True)
    horario = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)