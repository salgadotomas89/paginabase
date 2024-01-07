

from comunicados import views
from django.urls import path, include


urlpatterns = [
    path('seccion/color/<str:color>', views.actualizar_seccion_comunicados),
    path('guardar-comunicado/', views.guardar_comunicado, name='guardar_comunicado'),
    path('', views.comunicados, name='comunicados'),
]
