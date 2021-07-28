from django.db import models
from django.urls import reverse


class Vacancy(models.Model):
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['is_active', '-created_at']

    specialization = models.ForeignKey('team.Specialization', on_delete=PROTECT, blank=True, null=True,
                                       verbose_name='Специализация')
    name = models.CharField(max_length=255, verbose_name='Название вакансии')
    contract_type = models.ForeignKey('team.ContractType', on_delete=models.PROTECT, verbose_name='Тип договора')

    description = models.TextField(verbose_name='Описание', blank=True)
    responsibilities = models.ManyToManyField('Responsibilities', blank=True, verbose_name='Обязанности')
    requirements = models.ManyToManyField('Requirements', blank=True, verbose_name='Требования')
    conditions = models.ManyToManyField('Conditions', blank=True, verbose_name='Условия')

    is_active = models.BooleanField(default=True, blank=True, verbose_name='Вакансия актуальна')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата добавления')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('vacancy_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.is_active} {self.name} {self.created_at}'


class VacancyEnumeration(models.Model):
    """Базовый класс текстовых перечислений"""
    class Meta:
        abstract = True

    text = models.CharField(max_length=255, verbose_name='Содержание')

    def __str__(self):
        output = str(self.text)
        max_size = 50
        if len(output) > max_size:
            output = output[:max_size] + '...'
        return output


class Responsibilities(VacancyEnumeration):
    class Meta:
        verbose_name = 'Обязанность'
        verbose_name_plural = 'Обязанности'


class Requirements(VacancyEnumeration):
    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'


class Conditions(VacancyEnumeration):
    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'
