# Generated by Django 4.2 on 2023-05-08 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0003_noticia_tema_alter_noticia_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='noticia',
        ),
        migrations.AddField(
            model_name='noticia',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.images'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='fotos'),
        ),
    ]
