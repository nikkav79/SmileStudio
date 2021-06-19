from django.db import models

class StudioDescription(models.Model):
    "Описание студии"
    pass


class Specialization(models.Model):
    "Специализации/должности"
    pass

class Status(models.Model):
    "Характер договора"
    pass



class Staff(models.Model):
    "Сотрудники студии"
    pass


class Vacancy(models.Model):
    "Вакансии студии"
    pass



class AgeGroups(models.Model):
    "Возрастные группы"
    pass

class LessonsType(models.Model):
    "Тип занятий"
    pass

class AgeLessons(models.Model):
    "Таблица связи возрастной группы и типа занятий"
    pass

class Costs(models.Model):
    "Стоимость занятий"
    pass



class Lessons(models.Model):
    "Занятия"
    pass

class Media(models.Model):
    "Фото и видеоматериалы, их краткое описание"
    pass



class Reviews(models.Model):
    "Отзывы о преподавателях и студии"
    pass


class ContactDetails(models.Model):
    "Контактные данные студии"
    pass

class SocialNetworks(models.Model):
    "Ссылки на социальные сети"
    pass
