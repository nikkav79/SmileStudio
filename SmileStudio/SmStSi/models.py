from django.db import models


class Specialization(models.Model):
    """Специализации/должности"""
    name = models.CharField('Специализация', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class LessonsType(models.Model):
    """Тип занятий"""
    name = models.CharField('Специализация', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'


class StudioDescription(models.Model):
    """Описание студии"""
    pass

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
    pass

class SocialNetworks(models.Model):
    """Ссылки на социальные сети"""
    pass
