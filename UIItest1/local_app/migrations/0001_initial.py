# Generated by Django 5.1.1 on 2024-10-30 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='local',
            fields=[
                ('id_local', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('horario', models.DateTimeField(max_length=100)),
                ('ambiente', models.CharField(max_length=100)),
                ('servicios', models.CharField(max_length=100)),
                ('trabajadores', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
