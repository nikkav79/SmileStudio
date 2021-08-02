from django.db import models
from django.contrib.auth.models import User
from media.models import Media
from lessons.models import LessonsType
from django.shortcuts import reverse


class NewsFlow(models.Model):
    """ Новости портала """
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    digest = models.CharField(max_length=200, verbose_name='Краткое содержание', blank=True, null=True)
    content = models.TextField(verbose_name='Контент')
    media_url = models.URLField(default='', verbose_name='Медиассылка', blank=True,
                                null=True)  # вот тут надо подумать нужно ли
    media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Медиа', null=True, blank=True)
    topic = models.ForeignKey(LessonsType, on_delete=models.CASCADE, verbose_name='Тематика', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    slug = models.SlugField(max_length=150, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('news_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified', 'title']  # сортировка
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


