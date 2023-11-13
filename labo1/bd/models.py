from django.db import models

# Create your models here.

class Carreras(models.Model):
    ID_Carrera = models.IntegerField()
    Nombre_Carrera = models.CharField(max_length=100)

class Profesores(models.Model):
    ID_Profesor = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)

class Estudiantes(models.Model):
    ID_Estudiante = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Edad = models.IntegerField()
    Carrera_ID = models.IntegerField()

class Asignatura(models.Model):
    ID_Asignatura = models.IntegerField()
    Nombre_Asignatura = models.CharField(max_length=100)
    ID_Profesor = models.IntegerField()
    Carrera_ID = models.IntegerField()