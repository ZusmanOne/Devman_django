# Generated by Django 4.0.3 on 2022-04-22 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_description_long_alter_placeimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Локация'),
        ),
    ]
