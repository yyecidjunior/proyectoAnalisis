# Generated by Django 4.2.2 on 2023-10-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Gmail', models.EmailField(max_length=254)),
                ('Celular', models.CharField(max_length=12)),
                ('Direccion', models.CharField(max_length=255)),
            ],
        ),
    ]