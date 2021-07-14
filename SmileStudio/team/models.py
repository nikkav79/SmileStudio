from django.db import models
from media.models import Media


class Specialization(models.Model):
    """Специализации"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Position(models.Model):
    """Должности"""
    name = models.CharField(max_length=150, verbose_name='Наименование должности')
    description = models.CharField(max_length=150, verbose_name='Описание должности', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class ContractType(models.Model):
    """Характер договора"""
    name = models.CharField(max_length=100, verbose_name='Тип договора')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип договора'
        verbose_name_plural = 'Типы договора'


class Team(models.Model):
    """Сотрудники студии"""
    photo = models.ForeignKey(Media, on_delete=models.PROTECT, verbose_name='Фото сотрудника', blank=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    experience = models.IntegerField(verbose_name='Стаж', blank=True, null=True)
    education = models.TextField(default='', verbose_name='Образование', blank=True, null=True)
    specialization = models.ManyToManyField(Specialization, related_name='team_members', verbose_name='Специализации',
                                            blank=True)
    positions = models.ManyToManyField(Position, related_name='team_members', verbose_name='Должности', blank=True)
    contract = models.ForeignKey(ContractType, on_delete=models.CASCADE, verbose_name='Договор', blank=True, null=True)
    ad_information = models.TextField(verbose_name='ad_information', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name']


class Vacancy(models.Model):
    """Вакансии студии"""
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация')
    contract = models.ForeignKey(ContractType, on_delete=models.CASCADE, verbose_name='Статус')
    description = models.TextField(verbose_name='Описание')
    responsibilities = models.TextField(verbose_name='Обязанности')
    requirements = models.TextField(verbose_name='Требования')
    conditions = models.TextField(verbose_name='Условия')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['date_add']
