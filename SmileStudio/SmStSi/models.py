from django.db import models
from phone_field import PhoneField


class StudioDescription(models.Model):
    """Описание студии"""
    about = models.TextField('О нас')
    philosophy = models.TextField('Философия центра')
    mission = models.TextField('Наша миссия')
    sight = models.TextField('Наш взгляд')
    target = models.TextField('Наша цель')


class Specialization(models.Model):
    """Специализации/должности"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


class Status(models.Model):
    """Характер договора"""
    pass


class Staff(models.Model):
    """Сотрудники студии"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    experience = models.CharField(max_length=150)
    education = models.CharField(max_length=150)
    specialization_id = models.ForeignKey(Specialization)
    status_id = models.ForeignKey(Status)
    ad_information = models.TextField()


class Vacancy(models.Model):
    """Вакансии студии"""
    pass


class AgeGroups(models.Model):
    """Возрастные группы"""
    pass


class LessonsType(models.Model):
    """Тип занятий"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'


class AgeLessons(models.Model):
    """Таблица связи возрастной группы и типа занятий"""
    pass


class Lessons(models.Model):
    """Занятия"""
    pass


class Costs(models.Model):
    """Стоимость занятий"""
    lesson_type_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    cost = models.DecimalField(10, 2)


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
