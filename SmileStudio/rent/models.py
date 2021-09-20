from django.db import models
from media.models import Media

class Rent(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    about = models.TextField(verbose_name='Описание аренды')
    media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Медиа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'
