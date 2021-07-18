from django.db import models
from lessons.models import Lessons
from django.contrib.auth.models import User
from team.models import Team


class Reviews(models.Model):
    """Отзывы о преподавателях и студии"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='Занятие')
    team_member = models.ManyToManyField(Team, verbose_name='Сотрудник')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    message = models.TextField(verbose_name='Текст отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['date']
