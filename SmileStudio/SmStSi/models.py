from django.db import models
from phone_field import PhoneField



class StudioDescription(models.Model):
    """Описание студии"""
    pass



class Specialization(models.Model):
    """Специализации/должности"""
    name = models.CharField('Специализация', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Status(models.Model):
    """Характер договора"""
    pass


class Staff(models.Model):
    """Сотрудники студии"""
    pass


class Vacancy(models.Model):
    """Вакансии студии"""
    pass


class AgeGroups(models.Model):
    """Возрастные группы"""
    pass


class LessonsType(models.Model):
    """Тип занятий"""
    name = models.CharField('Специализация', max_length=50)
    description = models.TextField('Описание')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'



class AgeLessons(models.Model):
    """Таблица связи возрастной группы и типа занятий"""
    pass


class Costs(models.Model):
    """Стоимость занятий"""
    pass


class Lessons(models.Model):
    """Занятия"""
    pass


class Media(models.Model):
    """Фото и видеоматериалы, их краткое описание"""
    pass


class Reviews(models.Model):
    """Отзывы о преподавателях и студии"""
    pass


class ContactDetails(models.Model):
    """Контактные данные студии"""
    city = models.CharField(max_length=100, verbose_name='Город')
    district = models.CharField(max_length=150, verbose_name='Район')
    street = models.CharField(max_length=150, verbose_name='Улица')
    building = models.CharField(max_length=10, verbose_name='Дом')
    postcode = models.PositiveBigIntegerField(verbose_name='Индекс')
    phone = PhoneField(blank=True, help_text='Contact phone number', verbose_name='Телефон')
    email = models.EmailField(max_length=254, blank=True, verbose_name='Электронная почта')
    location = models.CharField(max_length=150, verbose_name='Расположение на карте', blank=True)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building}'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
        ordering = ['city']


class SocialNetworks(models.Model):
    """Ссылки на социальные сети"""
    name = models.CharField(max_length=100, blank=True, verbose_name='Название')
    link = models.CharField(max_length=254, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
        ordering = ['name']
