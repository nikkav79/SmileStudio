from django.db import models


class StudioDescription(models.Model):
    """Описание студии"""
    about = models.TextField('О нас')
    philosophy = models.TextField('Философия центра')
    mission = models.TextField('Наша миссия')
    sight = models.TextField('Наш взгляд')
    target = models.TextField('Наша цель')


class Specialization(models.Model):
    """Специализации/должности"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Status(models.Model):
    """Характер договора"""
    pass


class Staff(models.Model):
    """Сотрудники студии"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    specilaization_id = models.ForeignKey(Specialization)
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
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class AgeLessons(models.Model):
    """Таблица связи возрастной группы и типа занятий"""
    pass


class Costs(models.Model):
    """Стоимость занятий"""
    lessson_type_id = models.ForeignKey(Lessons, models.CASCADE())
    staff_id = models.ForeignKey(Staff, models.CASCADE())
    cost = models.FloatField()


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
    city = models.CharField(max_length=100)
    district = models.TextField()
    street = models.CharField(max_length=150)
    postcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.TextField()


class SocialNetworks(models.Model):
    """Ссылки на социальные сети"""
    name = models.CharField(max_length=50)
    links = models.TextField()
