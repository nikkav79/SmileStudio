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
    lessontype_age = models.ManyToManyField(AgeGroups, verbose_name='Возрастная группа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'


class Lessons(models.Model):
    """Занятия"""
    name = models.ForeignKey(LessonsType, verbose_name='Занятие', on_delete=models.CASCADE, null=True)
    team_member = models.ForeignKey(Team, verbose_name='Преподаватель', on_delete=models.CASCADE, null=True)
    cost = models.ManyToManyField('CostsParam', verbose_name='Цена')
    days = models.ManyToManyField('WeekDays', through='TimeTable',
                                  through_fields=('lessons', 'days'),
                                  verbose_name='Расписание')
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return f'{self.name}: {self.team_member}'

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'


class CostsParam(models.Model):
    """Стоимость занятий"""
    FORMAT = (('o', 'On-line'),
              ('s', 'В студии')
              )
    FORM_LESSONS = (('g', 'Групповое занятие'),
                    ('i', 'Индивидуальное'),
                    )
    PAYMENT_FORMAT = (('a', 'Абонемент'),
                      ('r', 'Разовое занятие'),
                      )
    format = models.CharField(max_length=1, choices=FORMAT, verbose_name='Место проведения')
    payment_fromat = models.CharField(max_length=1, choices=PAYMENT_FORMAT, verbose_name='Формат оплаты')
    form_lesson = models.CharField(max_length=1, choices=FORM_LESSONS, verbose_name='Форма проведения')
    duration = models.IntegerField(verbose_name='Длительность в минутах')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.format, self.payment_fromat, self.form_lesson, self.duration, self.cost}'

    class Meta:
        ordering = ['cost']
        verbose_name = 'Параметры занятия'
        verbose_name_plural = 'Параметры занятия'


class WeekDays(models.Model):
    """Дни недели"""
    day = models.CharField(max_length=11, verbose_name='День недели', default='')

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class TimeTable(models.Model):
    days = models.ForeignKey(WeekDays, on_delete=models.CASCADE, null=True)
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, null=True)
    time_start = models.TimeField(default='12:00:00')
