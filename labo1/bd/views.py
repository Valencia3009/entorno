from django.shortcuts import render
from .models import Carreras, Profesores, Estudiantes, Asignatura

# Create your views here.

def Lista(request):
    carreras = Carreras.objects.all()
    profesores = Profesores.objects.all()
    estudiantes = Estudiantes.objects.all()
    asignatura = Asignatura.objects.all()
    
    return render(request, 'bd.html',{'carreras':carreras, 'profesores': profesores, 
                                      'estudiantes':estudiantes, 'asignatura':asignatura})
