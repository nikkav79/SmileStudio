from django.db import models


class Media(models.Model):
    """Фото и видеоматериалы, их краткое описание"""
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    media_link = models.FileField(upload_to='post_files', blank=False, null=False, verbose_name='Ссылка на медиа-файл')
    short_description = models.CharField(max_length=127, verbose_name='Краткое описание', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='Выводится в галерею')

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'
        ordering = ['date']  # Как сделать, что бы по названию занятия или по фамилии педагога?


