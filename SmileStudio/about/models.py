from django.db import models
from phone_field import PhoneField
from media.models import Media


class StudioDescription(models.Model):
    """Описание студии"""
    about = models.TextField(default='', verbose_name='О нас', blank=True, null=True)
    logotype = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Логотип', blank=True, null=True)

    class Meta:
        verbose_name = 'О Нас'
        verbose_name_plural = 'О Нас'


class ContactDetails(models.Model):
    """Контактные данные студии"""
    city = models.CharField(max_length=100, verbose_name='Город')
    district = models.CharField(max_length=150, verbose_name='Район')
    street = models.CharField(max_length=150, verbose_name='Улица')
    building = models.CharField(max_length=10, verbose_name='Дом')
    postcode = models.PositiveBigIntegerField(verbose_name='Индекс')
    phone = PhoneField(blank=True, help_text='Contact phone number', verbose_name='Телефон')
    email = models.EmailField(max_length=254, blank=True, verbose_name='Электронная почта')
    location = models.CharField(max_length=150, verbose_name='Расположение на карте', blank=True, null=True)
    requisites = models.CharField(max_length=255, verbose_name='Реквизиты', blank=True, null=True)
    starting_work_weekdays = models.TimeField(verbose_name='Начало работы в будние', blank=True, null=True)
    finishing_work_weekdays = models.TimeField(verbose_name='Конец работы в будние', blank=True, null=True)
    starting_work_weekends = models.TimeField(verbose_name='Начало работы по выходным', blank=True, null=True)
    finishing_work_weekends = models.TimeField(verbose_name='Конец работы по выходным', blank=True, null=True)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building}'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
        ordering = ['city']


class SocialNetworks(models.Model):
    """Ссылки на социальные сети"""
    name = models.CharField(max_length=100, verbose_name='Название')
    link = models.CharField(max_length=254, verbose_name='Ссылка')

    # link_1 = models.SlugField(max_length=254, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
        ordering = ['name']


class Rent(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    about = models.TextField(verbose_name='Описание аренды')
    media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Медиа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'
