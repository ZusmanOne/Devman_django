from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(blank=True, null=True, verbose_name='Полное описание')
    coord_long = models.FloatField(verbose_name='Долгота')
    coord_lat = models.FloatField(verbose_name="Широта")

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['title']

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name='Путь изображения')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images',
                              verbose_name='Локация')
    number = models.PositiveIntegerField(db_index=True, default=0, verbose_name='Номер картинки')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place}'
