# Generated by Django 4.0.3 on 2022-04-20 17:00

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_rename_image_placeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Путь изображения'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Локация'),
        ),
    ]
