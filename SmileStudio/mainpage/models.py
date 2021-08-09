from django.db import models
from phone_field import PhoneField
from lessons.models import LessonsType


class WriteToUs(models.Model):
    """Данные пользователей для обратной связи"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    # phone = PhoneField(blank=True, help_text='Contact phone number', verbose_name='Телефон')
    email = models.EmailField(max_length=254, blank=True, verbose_name='Электронная почта')
    lesson_type = models.CharField(max_length=100, verbose_name='Занятие')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата контакта')

    class Meta:
        verbose_name = 'Напишите нам'
        verbose_name_plural = 'Напишите нам'
