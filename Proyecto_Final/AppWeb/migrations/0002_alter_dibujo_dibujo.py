# Generated by Django 4.1.5 on 2023-02-23 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dibujo',
            name='dibujo',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
