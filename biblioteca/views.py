from django.shortcuts import render

# Create your views here.


def biblioteca(request):

    return render(request, 'biblioteca.html')


def boletines(request):

    return render(request, 'boletines.html')