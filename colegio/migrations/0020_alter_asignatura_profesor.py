# Generated by Django 4.2 on 2023-08-14 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0019_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.userprofile'),
        ),
    ]
