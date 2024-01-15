from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.template.loader import render_to_string
from django.db.models import Q
# Desde cualquier archivo dentro de tus apps
from colegio.models import AppearanceSettings, Asignatura, Colegio, Curso, CursoAsignatura, Evento, UserProfile
from comunicados.models import Comunicado, Comunicados
from noticias.models import Images, Noticia
from .forms import AppearanceSettingsForm, CustomUserForm, FormEvento
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def not_found(request, exception):
    error_message = "Lo sentimos, la página que estás buscando no se encuentra disponible."
    return render(request, '404.html', {'error_message': error_message}, status=404)

#datos de acceso a admin salgadotomas, miercoles

from django.core import serializers

def obtener_usuarios_disponibles(request):
    if request.method == 'GET':
        # Filtra los usuarios por el rol 'profesor' en UserProfile
        usuarios_disponibles = UserProfile.objects.filter(Q(role='profesor'), Q(jefe=False))

        # Serializa los objetos UserProfile a JSON
        usuarios = [{'id': usuario.user.id, 'username': usuario.user.username} for usuario in usuarios_disponibles]

        # Devuelve los usuarios en formato JSON
        return JsonResponse({'success': True, 'usuarios': usuarios}, safe=False)
    else:
        # Maneja el caso si no es una solicitud GET
        data = {
            'success': False,
            'message': 'Método no permitido'
        }
        return JsonResponse(data)

def registro_profesor(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario
            form.save()
            # Puedes devolver una respuesta JSON con un mensaje de éxito
            return JsonResponse({"message": "Profesor guardado con éxito"})
        else:
            # Si el formulario no es válido, devuelve un error
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": "Solicitud no válida"}, status=400)

def usuarios(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios.html', context)


def dame_asignatura(request):
    if request.method == 'POST':
        asignatura_id = request.POST.get('asignaturaId')
        curso_id = request.POST.get('cursoId')
        # Ahora puedes realizar acciones con las variables recibidas
        # y devolver una respuesta JSON si es necesario
        try:
            asignatura = CursoAsignatura.objects.get(Q(asignatura_id=asignatura_id), Q(curso_id=curso_id))
            if asignatura.profesor:
                profesor_nombre = asignatura.profesor.user.first_name
            else:
                profesor_nombre = 'profesor no asignado'
            # Convierte el objeto UserProfile en un diccionario
            profesor_data = {
                'nombre': profesor_nombre
            }

            return JsonResponse({'success': True, 'profesor': profesor_data})
        except CursoAsignatura.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Asignatura no encontrada'})
    else:
        response_data = {'success': False}
        return JsonResponse(response_data)
    
def asignaturas(request):
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas': asignaturas
    }
    return render(request, 'asignaturas.html', context)

def nuevo_formato(fecha):
    print('hola')

def config(request):
    return render(request, 'configuracion.html')

#funcion que devuelve la vista para rellenar informacion sobre el colegio
#nombre, direccion, email principal, logo, etc
def ajustes(request):
    colegio = Colegio.objects.get()

    context = {
        "colegio": colegio
    }

    return render(request, 'informacion_colegio.html', context)


def obtener_profesor_jefe(request):
    if request.method == 'POST':
        curso_id = request.POST.get('cursoId')

        # Obtén el curso seleccionado
        curso = get_object_or_404(Curso, pk=curso_id)

        # Verifica si el curso tiene un profesor jefe asignado
        if curso.profesor_jefe:
            profesor_jefe = {
                'nombre': curso.profesor_jefe.user.username,
                'titulo': curso.profesor_jefe.role  # Aquí puedes agregar el campo correcto de UserProfile que almacena el título
            }
        else:
            profesor_jefe = {
                'nombre': 'No asignado',
                'titulo': 'No asignado'
            }

        # Devuelve los detalles del profesor jefe en formato JSON
        data = {
            'success': True,
            'profesor': profesor_jefe
        }
        return JsonResponse(data)

    # Maneja el caso si no es una solicitud POST
    data = {
        'success': False,
        'message': 'Método no permitido'
    }
    return JsonResponse(data)

def guardar_asignatura(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nueva_asignatura = Asignatura(nombre=nombre)
        nueva_asignatura.save()

        # Obtener la lista actualizada de asignaturas después de guardar
        asignaturas = Asignatura.objects.all()
        asignaturas_info = [{'id': asignatura.id, 'nombre': asignatura.nombre} for asignatura in asignaturas]

        return JsonResponse({'success': True, 'asignaturas': asignaturas_info})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})

def guardar_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreCurso')
        curso = Curso(nombre=nombre)
        curso.save()
         # Obtén la lista actualizada de cursos
        cursos = Curso.objects.all()
        cursos_list = [{'id': curso.id, 'nombre': curso.nombre} for curso in cursos]

        # Devuelve la lista de cursos en formato JSON
        return JsonResponse({'success': True, 'cursos': cursos_list})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})

def obtener_asignaturas(request):
    if request.method == 'POST':
        curso_id = request.POST.get('cursoId')

        try:
            curso = Curso.objects.get(id=curso_id)
            asignaturas_inscritas = curso.asignaturas.all()
            
            context = {'asignaturas': asignaturas_inscritas}
            asignaturas_html = render_to_string('asignaturas_list.html', context)
            
            return JsonResponse({'success': True, 'asignaturas_html': asignaturas_html})
        except Curso.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Curso no encontrado'})
    else:
        asignaturas = Asignatura.objects.all()
        context = {'asignaturas': asignaturas}
        asignaturas_html = render_to_string('asignaturas_list.html', context)
        return JsonResponse({'success': True, 'asignaturas_html': asignaturas_html})

def asignar_asignaturas(request):
    if request.method == 'POST':
        curso_id = request.POST.get('cursoId')
        asignaturas_seleccionadas = request.POST.getlist('asignaturas[]')

        try:
            curso = get_object_or_404(Curso, id=curso_id)
            asignaturas_actuales = list(curso.asignaturas.all())  # Obtener las asignaturas actuales como una lista

            # Agregar las nuevas asignaturas a la lista existente
            for asignatura_id in asignaturas_seleccionadas:
                asignatura = Asignatura.objects.get(id=asignatura_id)
                asignaturas_actuales.append(asignatura)

            # Actualizar el conjunto de asignaturas en el curso
            curso.asignaturas.set(asignaturas_actuales)

            # Guardar el curso u realizar cualquier otro paso necesario
            curso.save()
            asignaturas = list(curso.asignaturas.all())

            context = {'asignaturas': asignaturas}
            asignaturas_html = render_to_string('asignaturas_list.html', context)
                
            return JsonResponse({'success': True, 'asignaturas_html': asignaturas_html})
        except Curso.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Curso no encontrado'})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})

def calendario_evaluaciones(request):
    cursos = Curso.objects.all()
    print(cursos)
    context = {
        "cursos": cursos,
    }
    return render(request, 'calendario_evaluaciones.html', context)


def eliminar_asignatura(request):
    if request.method == 'POST':
        curso_id = request.POST.get('cursoId')
        asignatura_id = request.POST.get('asignatura_id')

        if curso_id :
            try:
                asignatura = CursoAsignatura.objects.get(Q(asignatura_id=asignatura_id), Q(curso_id=curso_id))
                asignatura.delete()

                return JsonResponse({'success': True})
            except CursoAsignatura.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Asignatura no encontrada'})
        else:
            try:
                print('id asignatura')
                print(asignatura_id)
                asignatura = Asignatura.objects.get(id=asignatura_id)
                asignatura.delete()

                return JsonResponse({'success': True})
            except CursoAsignatura.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Asignatura no encontrada'})
    else:
        return JsonResponse({'success': False, 'error': 'metodo de solicitud no valido'})

def asignar_profesor_asignatura(request):
    if request.method == 'POST':
        asignatura_id = request.POST.get('asignaturaId')
        profesor_id = request.POST.get('profesorId')
        curso_id = request.POST.get('cursoId')

        try:
            asignatura = CursoAsignatura.objects.get(Q(asignatura_id=asignatura_id), Q(curso_id=curso_id))
            profesor = UserProfile.objects.get(user_id=profesor_id)
            asignatura.profesor = profesor
            asignatura.save()
            
            # Update the professor for the selected subject
            return JsonResponse({'success': True})
        except (Asignatura.DoesNotExist, UserProfile.DoesNotExist):
            return JsonResponse({'success': False, 'error': 'Asignatura o profesor no encontrado'})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})



def cursos(request):
    asignaturas = Asignatura.objects.all()
    
    cursos = Curso.objects.all()
    # Filtrar los usuarios con rol de "profesor"
    profesores = UserProfile.objects.filter(role='profesor')


    context = {
        "asignaturas": asignaturas,
        "cursos": cursos,
        "profesores": profesores,
    }

    return render(request, 'config/cursos.html', context)


def eliminar_asignatura_de_curso(request):
    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura_id')
        curso_id = request.POST.get('curso_id')

        

        try:
            curso = Curso.objects.get(id=curso_id)
            asignatura = Asignatura.objects.get(id=asignatura_id)
            curso.asignaturas.remove(asignatura)

            asignaturas = list(curso.asignaturas.all())

            context = {'asignaturas': asignaturas}
            asignaturas_html = render_to_string('asignaturas_list.html', context)
                
            return JsonResponse({'success': True, 'asignaturas_html': asignaturas_html})
        except (Curso.DoesNotExist, Asignatura.DoesNotExist):
            return JsonResponse({'success': False, 'error': 'Curso o asignatura no encontrados'})

    return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})


def asignar_profesor_jefe(request):

    if request.method == 'POST':
        curso_id = request.POST.get('cursoId')
        profesor_id = request.POST.get('profesor')
        profesor = UserProfile.objects.get(user_id=profesor_id)
        
        curso = Curso.objects.get(id=curso_id)
        curso.profesor_jefe = profesor
        curso.save()
        
        profesor.jefe = True
        profesor.save()
        print('hello')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})

def quitar_profesor_jefe(request):
    print('hola ')
    if request.method == 'POST':
        curso_id = request.POST.get('cursoId')
        curso = Curso.objects.get(id=curso_id)
        user = User.objects.get(username=curso.profesor_jefe)
        profesor  =  UserProfile.objects.get(user_id = user.id)
        profesor.jefe = False
        profesor.save()

        curso.profesor_jefe = None
        curso.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'No se pudo eliminar profesor jefe' })

def actualizar_email_colegio(request):
    print('guardando email de colegio')
    nuevo_email = request.POST.get('nuevo_email')

    colegio = Colegio.objects.first()  # Obtener el único objeto del modelo Colegio
    colegio.email = nuevo_email
    colegio.save()

    return JsonResponse({'success': True})

def actualizar_horario_colegio(request):
    print('guardando horario de colegio')
    nuevo_horario = request.POST.get('nuevo_horario')

    colegio = Colegio.objects.first()  # Obtener el único objeto del modelo Colegio
    colegio.horario = nuevo_horario
    colegio.save()

    return JsonResponse({'success': True})

def actualizar_nombre_colegio(request):
    print('guardando nombre colegio')
    nuevo_nombre = request.POST.get('nuevo_nombre')

    colegio = Colegio.objects.first()  # Obtener el único objeto del modelo Colegio
    colegio.nombre = nuevo_nombre
    colegio.save()

    return JsonResponse({'success': True})

def actualizar_direccion_colegio(request):
    print('guardando direccion colegio')
    nueva = request.POST.get('nueva_direccion')

    colegio = Colegio.objects.first()  # Obtener el único objeto del modelo Colegio
    colegio.direccion = nueva
    colegio.save()

    return JsonResponse({'success': True})

def actualizar_telefono_colegio(request):
    print('guardando telefono colegio')
    nuevo = request.POST.get('nuevo_telefono')

    colegio = Colegio.objects.first()  # Obtener el único objeto del modelo Colegio
    colegio.telefono = nuevo
    colegio.save()

    return JsonResponse({'success': True})

def directiva(request):
    context = {'lista': ['directiva','misión', 'visión', 'direccion', 'reglamentos']
}
    return render(request, 'directiva.html', context)

#devuelve la vista para ver a todos los profesores del colegio
def profesores(request):
    return render(request, 'profesores.html')

def inicio(request):
    
    comunicados = Comunicado.objects.all().order_by('-fecha')[:5]
    eventos = Evento.objects.all().order_by('-fecha')[:4]
    noticias = Noticia.objects.all()
    form = CustomUserForm()  # Crear una instancia del formulario

    try:
        seccion_comunicado = Comunicados.objects.get()
    except Comunicados.DoesNotExist:
        seccion_comunicado = None

    context = {
               'comunicado': seccion_comunicado,
               'comunicados': comunicados,
               'noticias': noticias,
               'eventos': eventos,
               'form_usuario' : form,
               }
    
    return render(request, 'home.html', context)



def registro(request):
    if request.method == 'POST':
        user_form = CustomUserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            role = user_form.cleaned_data.get('role')
            user.save()
            if role:
                UserProfile.objects.create(user=user, role=role)
            return redirect('home')
        else:
            print('Error en el formulario:', user_form.errors)
    else:
        user_form = CustomUserForm()
    return render(request, 'registration/form.html', {'form': user_form})




#funcion de salir usuarios
def exit(request):
    logout(request)
    return redirect('home')

def fotos(request):

    noticias = Noticia.objects.all()
    noticias_ordenadas = noticias.order_by('-date')
    #aqui guardare solo las noticias que tengan fotos para mostrar en la galeria
    noticias_galeria = []

    for n in noticias_ordenadas:
        n.date = nuevo_formato(n.date)  # actualizo su formato de fecha
        #si la noticia.galeria es verdadera
        if n.galeria == True:
            #agrego la noticia en la lista
            noticias_galeria.append(n)

    #traigo todas las fotos de noticias
    fotos = Images.objects.all()
    
    return render(request, 'fotos/galeria.html', {'noticias':noticias_galeria, 'fotos':fotos})  




def guardar_evento(request):
    if request.method == 'POST':
        # Acceder a los datos del comunicado enviados en la solicitud
        guia = FormEvento(request.POST)
        if guia.is_valid():
            guia.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})


def apariencia(request):
    apariencia = AppearanceSettings.objects.first()
    if not apariencia:
        apariencia = AppearanceSettings.objects.create()

    if request.method == 'POST':
        form = AppearanceSettingsForm(request.POST, instance=apariencia)
        if form.is_valid():
            form.save()
            # Podrías redirigir a la misma página para ver los cambios
            return redirect('inicio')

    else:
        print('hello')
        form = AppearanceSettingsForm(instance=apariencia)

    current_section = request.GET.get('section', None)

    context = {
        'current_section': current_section,
        'apariencia': apariencia,
        'form': form
    }

    return render(request, 'apariencia.html', context)

def menu(request):
    return render(request, 'menu.html')

def configuracion(request):
    apariencia = AppearanceSettings.objects.first()
    if not apariencia:
        apariencia = AppearanceSettings.objects.create()

    if request.method == 'POST':
        form = AppearanceSettingsForm(request.POST, instance=apariencia)
        if form.is_valid():
            form.save()
            # Podrías redirigir a la misma página para ver los cambios
            return redirect('home')

    else:
        form = AppearanceSettingsForm(instance=apariencia)

    current_section = request.GET.get('section', None)

    context = {
        'current_section': current_section,
        'apariencia': apariencia,
        'form': form
    }

    return render(request, 'configuracion.html', context)