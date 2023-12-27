


from colegio.models import Colegio


def datos_globales(request):
    colegio = Colegio.objects.first()  # Obtener el único objeto del modelo Colegio

   

    lista =  ['directiva','misión', 'visión', 'direccion', 'reglamentos']

              
               
    return {
        'colegio': colegio,
        'lista': lista,
    }