from django.contrib import admin

from colegio.models import  Evento, Colegio
from comunicados.models import Comunicados

# Register your models here.
admin.site.register(Evento)
admin.site.register(Colegio)
admin.site.register(Comunicados)

