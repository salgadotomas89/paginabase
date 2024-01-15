from django.urls import include, path
from . import views
# Importa la vista creada anteriormente
from colegio.views import not_found

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('configuracion', views.configuracion, name='configuracion'),

    path('registro', views.registro, name='registro'),
    path('registro/profesor', views.registro_profesor, name='registro_profesor'),

    path('logout', views.exit, name="exit"),
    path('config', views.config, name='config'),
    path('eliminar_asignatura_de_curso/', views.eliminar_asignatura_de_curso, name='eliminar_asignatura_de_curso'),

    path('guardar_asignatura', views.guardar_asignatura, name="guardar_asignatura"),

    path('guardar_curso', views.guardar_curso, name="guardar_curso"),

    path('asignar_asignaturas', views.asignar_asignaturas, name="asignar_asignaturas"),

    path('obtener_profesor_jefe', views.obtener_profesor_jefe, name='obtener_profesor_jefe'),
    path('obtener_usuarios_disponibles', views.obtener_usuarios_disponibles, name='obtener_usuarios_disponibles'),
    path('usuarios', views.usuarios, name="usuarios"),
    path('cursos', views.cursos, name='cursos'),
    path('fotos', views.fotos, name='fotos'),
    path('asignar_profesor_jefe', views.asignar_profesor_jefe, name="asignar_profesor_jefe"),
    path('quitar_profesor_jefe', views.quitar_profesor_jefe, name="quitar_profesor_jefe"),
    path('directiva', views.directiva, name="directiva"),
    path('profesores', views.profesores, name='profesores'),
    path('ajustes', views.ajustes, name='ajustes'),

    path('asignaturas', views.asignaturas, name="asignaturas"),


    path('obtener_asignaturas', views.obtener_asignaturas, name="obtener_asignaturas"),
    path('eliminar_asignatura', views.eliminar_asignatura, name="eliminar_asignatura"),
    path('asignar_profesor_asignatura', views.asignar_profesor_asignatura, name="asignar_profesor_asignatura"),
    
    path('guardar-evento/', views.guardar_evento, name='guardar_evento'),

    path('dame_asignatura', views.dame_asignatura, name="dame_asignatura"),

    path('calendario_evaluaciones', views.calendario_evaluaciones, name="calendario_evaluaciones"),

    path('apariencia', views.apariencia, name="apariencia"),

    path('menu', views.menu, name="menu"),

    path('actualizar/', views.actualizar_nombre_colegio, name='actualizar_nombre_colegio'),
    path('actualizar-email/', views.actualizar_email_colegio, name='actualizar_email_colegio'),
    path('actualizar-direccion/', views.actualizar_direccion_colegio, name='actualizar_direccion_colegio'),
    path('actualizar-telefono/', views.actualizar_telefono_colegio, name='actualizar_telefono_colegio'),
    path('actualizar-horario/', views.actualizar_horario_colegio, name='actualizar_horario_colegio'),
]

handler404 = not_found