# Generated by Django 4.2 on 2023-06-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0013_colegio'),
    ]

    operations = [
        migrations.AddField(
            model_name='colegio',
            name='telefono',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='texto',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
