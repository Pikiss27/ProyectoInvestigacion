# Generated by Django 5.1.2 on 2024-11-18 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('area_trabajo', models.CharField(max_length=50)),
                ('nivel_instruccion', models.CharField(max_length=50)),
                ('antiguedad', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=50)),
                ('auto_identificacion_etnica', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
