# Generated by Django 4.2 on 2023-12-24 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0025_userprofile_jefe'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppearanceSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('menu_text_color', models.CharField(default='#000000', max_length=7)),
                ('menu_height', models.PositiveIntegerField(default=80, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(200)])),
                ('mega_menu_background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('mega_menu_text_color', models.CharField(default='#000000', max_length=7)),
                ('color_principal_texto', models.CharField(default='#000000', max_length=7)),
            ],
        ),
    ]
