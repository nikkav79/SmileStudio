from django.db import models
from django.contrib.auth.models import User
from media.models import Media
from contacts.models import ContactDetails
from django.shortcuts import reverse


class NewsFlow(models.Model):
    """ Новости портала """
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    digest = models.CharField(max_length=200, verbose_name='Краткое содержание', blank=True, null=True)
    content_main = models.TextField(verbose_name='Основной контент', blank=True, null=True)
    content_additional = models.TextField(verbose_name='Дополнительный контент', blank=True, null=True)
    content_selling = models.TextField(verbose_name='Контент для продажи', blank=True, null=True)
    content_contacts = models.ForeignKey(ContactDetails, on_delete=models.CASCADE, verbose_name="Контент с контактами",
                                         blank=True, null=True)
    media_url = models.URLField(default='', verbose_name='Медиассылка', blank=True,
                                null=True)
    media = models.ManyToManyField(Media, verbose_name='Медиа', related_name='media', null=True, blank=True)
    picture = models.FileField(upload_to='static/news/image/%Y.%m.%d/', verbose_name='Картинка новости', blank=True,
                               null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    tags = models.ManyToManyField('Newstag', blank=True, related_name='newstag')
    slug = models.SlugField(max_length=150, verbose_name='URL')
    is_active = models.BooleanField(verbose_name='Новость активна', blank=False, null=False, default=True)

    def get_absolute_url(self):
        return reverse('news_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-modified', 'title']  # сортировка
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class NewsTag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэг')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка', unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
