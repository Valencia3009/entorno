# Generated by Django 4.2.7 on 2023-11-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Asignatura', models.IntegerField()),
                ('Nombre_Asignatura', models.CharField(max_length=100)),
                ('ID_Profesor', models.IntegerField()),
                ('Carrera_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Carrera', models.IntegerField()),
                ('Nombre_Carrera', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Estudiante', models.IntegerField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Edad', models.IntegerField()),
                ('Carrera_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Profesor', models.IntegerField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
            ],
        ),
    ]