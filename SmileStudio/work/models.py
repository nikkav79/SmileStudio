from django.db import models
from team.models import Specialization, ContractType


class Vacancy(models.Model):
    """Вакансии"""
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация')
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE, verbose_name='Тип договора')
    slug = models.SlugField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Вакансия открыта')

    description = models.TextField(verbose_name='Описание', blank=True)
    responsibilities = models.TextField(verbose_name='Обязанности', blank=True)
    requirements = models.TextField(verbose_name='Требования', blank=True)
    conditions = models.TextField(verbose_name='Условия', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'{self.specialization} {self.created_at} {self.is_active}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['created_at']
