from django.urls import path
from . import views

urlpatterns = [
    path('', views.biblioteca, name='biblioteca'),
    path('boletines', views.boletines, name="boletines"),
]
