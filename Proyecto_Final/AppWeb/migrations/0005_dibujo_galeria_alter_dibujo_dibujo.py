# Generated by Django 4.1.5 on 2023-02-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0004_alter_dibujo_dibujo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dibujo',
            name='galeria',
            field=models.CharField(choices=[('galeria', 'Galeria'), ('dibujo', 'Dibujos')], default='galeria', max_length=15),
        ),
        migrations.AlterField(
            model_name='dibujo',
            name='dibujo',
            field=models.ImageField(blank=True, null=True, upload_to='AppWeb/imagenes/'),
        ),
    ]
