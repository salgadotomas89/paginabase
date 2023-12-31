# Generated by Django 4.2 on 2023-08-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0023_curso_profesor_jefe_cursoasignatura_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivoscomunicado',
            name='comunicado',
        ),
        migrations.DeleteModel(
            name='Comunicados',
        ),
        migrations.AlterField(
            model_name='curso',
            name='asignaturas',
            field=models.ManyToManyField(blank=True, null=True, through='colegio.CursoAsignatura', to='colegio.asignatura'),
        ),
        migrations.DeleteModel(
            name='ArchivosComunicado',
        ),
        migrations.DeleteModel(
            name='Comunicado',
        ),
    ]
