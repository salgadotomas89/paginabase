from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id>', views.noticias, name='noticias'),
    path('delete/<int:id>', views.destroy_noticia, name='delete_noticia'),

]