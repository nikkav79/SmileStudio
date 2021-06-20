from django.db import models
from phone_field import PhoneField


class StudioDescription(models.Model):
    """Описание студии"""
    about = models.TextField('О нас')
    philosophy = models.TextField('Философия центра')
    mission = models.TextField('Наша миссия')
    sight = models.TextField('Наш взгляд')
    target = models.TextField('Наша цель')


class Specialization(models.Model):
    """Специализации/должности"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

###
class Status(models.Model):
    """Характер договора"""
    name = models.CharField(max_length=100, verbose_name='Тип договора')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип договора'
        verbose_name_plural = 'Типы договора'


class Staff(models.Model):
    """Сотрудники студии"""

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    experience = models.CharField(max_length=150, verbose_name='Опыт')
    education = models.CharField(max_length=150, verbose_name='Образование')
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    ad_information = models.TextField()
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.experience}, {self.education}, {self.ad_information}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name']
###
class Vacancy(models.Model):
    """Вакансии студии"""
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    responsibilities = models.TextField(verbose_name='Обязанности')
    requirements = models.TextField(verbose_name='Требования')
    conditions = models.TextField(verbose_name='Условия')
    date_add = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name='Дата')
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['date_add']

###
class AgeGroups(models.Model):
    """Возрастные группы"""
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание ')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Возрастная группа'
        verbose_name_plural = 'Возрастные группы'

class LessonsType(models.Model):
    """Тип занятий"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'



class Costs(models.Model):
    """Стоимость занятий"""
    lesson_type_id = models.ForeignKey(LessonsType, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    cost = models.DecimalField(10, 2, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимости'


class Lessons(models.Model):
    """Занятия"""
    lesson_type_id = models.ForeignKey(LessonsType, on_delete=models.CASCADE)
    cost_id = models.ForeignKey(Costs, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50, verbose_name='Длительность')
    days = models.CharField(max_length=100, verbose_name='Дни')
    hours = models.CharField(max_length=100, verbose_name='Часы')
    lesson_age = models.ManyToManyField(AgeGroups)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'


class Media(models.Model):
    """Фото и видеоматериалы, их краткое описание"""
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    staff_id = models.ManyToManyField(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name='Дата')
    photo_link = models.ImageField(upload_to='post_files', blank=False, null=False)
    video_file = models.FileField(upload_to='post_files',blank=True,null=True)

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'
        ordering = ['date'] #Как сделать, что бы по названию занятия или по фамилии педагога?

###
class Reviews(models.Model):
    """Отзывы о преподавателях и студии"""
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    staff_id = models.ManyToManyField(Staff)
    date = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name='Дата')
    message = models.TextField()
    star_choice_1 = models.CharField(max_length=5, verbose_name='Рейтинг1')
    star_choice_2 = models.CharField(max_length=5, verbose_name='Рейтинг2')
    star_choice_3 = models.CharField(max_length=5, verbose_name='Рейтинг3')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['date']


class ContactDetails(models.Model):
    """Контактные данные студии"""

    city = models.CharField(max_length=100, verbose_name='Город')
    district = models.CharField(max_length=150, verbose_name='Район')
    street = models.CharField(max_length=150, verbose_name='Улица')
    building = models.CharField(max_length=10, verbose_name='Дом')
    postcode = models.PositiveBigIntegerField(verbose_name='Индекс')
    phone = PhoneField(blank=True, help_text='Contact phone number', verbose_name='Телефон')
    email = models.EmailField(max_length=254, blank=True, verbose_name='Электронная почта')
    location = models.CharField(max_length=150, verbose_name='Расположение на карте', blank=True)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building}'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
        ordering = ['city']


class SocialNetworks(models.Model):
    """Ссылки на социальные сети"""

    name = models.CharField(max_length=100, blank=True, verbose_name='Название')
    link = models.CharField(max_length=254, blank=True, verbose_name='Ссылка')
    #link_1 = models.SlugField(max_length=254, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
        ordering = ['name']
