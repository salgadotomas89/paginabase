# Generated by Django 4.2 on 2023-05-26 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0009_alter_evento_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
