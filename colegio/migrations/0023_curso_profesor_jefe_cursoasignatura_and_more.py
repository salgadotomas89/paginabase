# Generated by Django 4.2 on 2023-08-16 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0022_remove_asignatura_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='profesor_jefe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curso_profesor_jefe', to='colegio.userprofile'),
        ),
        migrations.CreateModel(
            name='CursoAsignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.asignatura')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='colegio.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='asignaturas',
            field=models.ManyToManyField(through='colegio.CursoAsignatura', to='colegio.asignatura'),
        ),
    ]
