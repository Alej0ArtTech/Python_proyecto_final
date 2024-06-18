# Generated by Django 5.0.6 on 2024-06-18 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('productos', '0002_remove_productoimagen_imagen_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
