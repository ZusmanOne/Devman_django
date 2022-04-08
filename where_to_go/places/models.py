from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, verbose_name='Полное описание')
    coord_long = models.FloatField(verbose_name='Долгота')
    coord_lat = models.FloatField(verbose_name="Широта")

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['title']

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="image/%Y/%m/%d", blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True, related_name='image')
    number = models.PositiveIntegerField(db_index=True, verbose_name='Номер картинки')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-number']

    def __str__(self):
        return "%s %s" % (self.number, self.place)




