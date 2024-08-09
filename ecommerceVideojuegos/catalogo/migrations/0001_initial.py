# Generated by Django 5.0.3 on 2024-07-30 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mensaje', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=50, null=True)),
                ('precio', models.IntegerField(default=0, null=True)),
                ('fecha_lanzamiento', models.DateTimeField()),
                ('genero', models.CharField(max_length=50, null=True)),
                ('plataforma', models.CharField(max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(default='imagenes/juegoComprar1.png', upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina_web', models.CharField(max_length=30, null=True)),
                ('nombre_empresa', models.CharField(max_length=30, null=True)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.producto')),
            ],
        ),
    ]