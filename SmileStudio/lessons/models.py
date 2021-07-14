from django.db import models
from media.models import Media
from team.models import Team


class AgeGroups(models.Model):
    """Возрастные группы"""
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Возрастная группа'
        verbose_name_plural = 'Возрастные группы'


class LessonsType(models.Model):
    """Тип занятий"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.ForeignKey(Media, on_delete=models.PROTECT, verbose_name='Фото', blank=True, null=True)
    improves_skills = models.CharField(max_length=255, verbose_name='Развивающиеся навыки', blank=True, null=True)
    group_lesson = models.BooleanField(default=True, verbose_name='Групповое занятие')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'


class Costs(models.Model):
    """Стоимость занятий"""
    lesson_type = models.ForeignKey(LessonsType, on_delete=models.CASCADE, verbose_name='Тип занятия')
    team_member = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Сотрудник')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.lesson_type}, {self.cost}, {self.team_member}'

    class Meta:
        ordering = ['lesson_type', 'team_member']
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимости'


class WeekDays(models.Model):
    """Дни недели"""
    day = models.CharField(max_length=11, verbose_name='День недели', default='')

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Lessons(models.Model):
    """Занятия"""
    name = models.ForeignKey(LessonsType, verbose_name='Занятие', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')
    lesson_age = models.ManyToManyField(AgeGroups, verbose_name='Возрастная группа')
    cost = models.ForeignKey(Costs, on_delete=models.CASCADE, verbose_name='Цена')
    days = models.ManyToManyField(WeekDays, through='TimeTable', through_fields=('lessons', 'days'),
                                  verbose_name='Расписание')
    duration = models.IntegerField(verbose_name='Длительность в минутах')

    def __str__(self):
        return f'{self.name}: {self.cost.team_member}'

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'


class TimeTable(models.Model):
    days = models.ForeignKey(WeekDays, on_delete=models.CASCADE, null=True)
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, null=True)
    time_start = models.TimeField(default='12:00:00')
