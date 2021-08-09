from django.db import models
from media.models import Media


class StudioDescription(models.Model):
    """Описание студии"""
    about = models.TextField(default='', verbose_name='О нас', blank=True, null=True)
    logotype = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Логотип', blank=True, null=True)

    class Meta:
        verbose_name = 'О Нас'
        verbose_name_plural = 'О Нас'

