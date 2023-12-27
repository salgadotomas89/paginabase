# Generated by Django 4.2 on 2023-05-24 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0006_comunicados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(blank=True, default='Mauricio Orellana', max_length=100, null=True)),
                ('texto', models.TextField(max_length=1000)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='comunicados',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comunicados'),
        ),
        migrations.CreateModel(
            name='ArchivosComunicado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='comunicados')),
                ('comunicado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.comunicado')),
            ],
        ),
    ]
