from datetime import datetime
from django.shortcuts import redirect, render
from django.http import Http404, JsonResponse
from noticias.forms import FormNoticia
from noticias.models import Images, Noticia



def noticias(request, id):
    otras_noticias = None
    ultima_noticia = None

    try:
        if id != 0:  # Si elegí alguna noticia en particular, la traigo con su id
            ultima_noticia = Noticia.objects.get(id=id)
            # Traigo las últimas 2 noticias excluyendo el elemento elegido por el id
            otras_noticias = Noticia.objects.exclude(id=id).order_by('-date')[:2]
        else:  # Si elegí la sección noticias
            # Comprobar si la tabla Noticias está vacía
            noticia = Noticia.objects.first()

            if noticia is None:
                print("La tabla Noticias está vacía, no hay objetos.")
            else:
                print("La tabla Noticias contiene al menos un objeto.")
                # Asigno la noticia más reciente como principal
                ultima_noticia = Noticia.objects.latest('date')
                otras_noticias = Noticia.objects.exclude(id=ultima_noticia.id)[:2]  # Puedes ajustar el número de noticias aquí

    except Noticia.DoesNotExist:
        error_message = "La noticia solicitada no existe."
        return render(request, '404.html' , {'error_message': error_message}, status=404)

    # Año actual
    currentYear = datetime.now().year
    currentMonth = datetime.now().month
    # Meses del año en el que hay actividades, enero y febrero no hay clases
    meses = ('marzo', 'abril', 'mayo', 'junio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

    data = {
        'año': currentYear,
        'meses': meses,
        'noticias': otras_noticias,
        'principal': ultima_noticia,
    }

    if request.method == 'POST':
        form_noticia = FormNoticia(request.POST, request.FILES)
        fotos = request.FILES.getlist('imagenes')

        if form_noticia.is_valid():
            noticia = form_noticia.save(commit=False)
            noticia.save()
            for f in fotos:
                foto = Images(noticia=noticia, image=f)
                foto.save()

            return redirect("noticias", id=0)
        else:
            print('Error al ingresar noticia:')
            print(form_noticia.errors)

    return render(request, 'noticias.html', data)




def destroy_noticia(request, id):
    try:
        news = Noticia.objects.get(id=id)
        news.delete()
        response_data = {'message': 'Noticia eliminada exitosamente'}
    except Noticia.DoesNotExist:
        response_data = {'error': 'La noticia que intentas eliminar no existe'}
    
    return JsonResponse(response_data)