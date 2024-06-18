# Generated by Django 5.0.6 on 2024-06-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoimagen',
            name='imagen_url',
        ),
        migrations.AddField(
            model_name='productoimagen',
            name='imagen',
            field=models.ImageField(default='img_producto/image_default.jpeg', upload_to='img_producto/'),
        ),
    ]
