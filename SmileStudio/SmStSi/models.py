from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User


class Specialization(models.Model):
    """Специализации/должности"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

class Position(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование должности')
    description = models.CharField(max_length=150, verbose_name='Описание должности', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

###
class ContractType(models.Model):
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
    experience = models.CharField(max_length=150, verbose_name='Опыт', blank=True, null=True)
    education = models.CharField(max_length=150, verbose_name='Образование', blank=True, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация',
                                       blank=True, null=True)
    contract = models.ForeignKey(ContractType, on_delete=models.CASCADE, verbose_name='Статус', blank=True, null=True)
    ad_information = models.TextField(verbose_name='ad_information', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name', 'first_name']


###
class Vacancy(models.Model):
    """Вакансии студии"""
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация')
    contract = models.ForeignKey(ContractType, on_delete=models.CASCADE, verbose_name='Статус')
    description = models.TextField(verbose_name='Описание')
    responsibilities = models.TextField(verbose_name='Обязанности')
    requirements = models.TextField(verbose_name='Требования')
    conditions = models.TextField(verbose_name='Условия')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['date_add']


###
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
    description = models.CharField(max_length=150, verbose_name='Описание', blank=True, null=True)
    improves_skills = models.CharField(max_length=255, verbose_name='Развивающиеся навыки', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'


class Costs(models.Model):
    """Стоимость занятий"""
    lesson_type = models.ForeignKey(LessonsType, on_delete=models.CASCADE, verbose_name='Тип занятия')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Сотрудник')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.lesson_type}, {self.cost}, {self.staff}'

    class Meta:
        ordering = ['lesson_type', 'staff']
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимости'


class Lessons(models.Model):
    """Занятия"""
    lesson_type = models.ForeignKey(LessonsType, on_delete=models.CASCADE, verbose_name='Тип урока')
    cost = models.ForeignKey(Costs, on_delete=models.CASCADE, verbose_name='Цена')
    duration = models.CharField(max_length=50, verbose_name='Длительность')
    days = models.CharField(max_length=100, verbose_name='Дни')
    hours = models.CharField(max_length=100, verbose_name='Часы')
    lesson_age = models.ManyToManyField(AgeGroups, verbose_name='Возрастная группа')
    is_active = models.BooleanField(default=True, verbose_name='Актив')

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'


class Media(models.Model):
    """Фото и видеоматериалы, их краткое описание"""
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='Занятие', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    photo_link = models.ImageField(upload_to='post_files', blank=False, null=False, verbose_name='Ссылка на фото')
    video_file = models.FileField(upload_to='post_files', blank=True, null=True, verbose_name='Ссылка на видео')
    short_description = models.CharField(max_length=127, verbose_name='Краткое описание', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='Выводится в галерею')

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'
        ordering = ['date']  # Как сделать, что бы по названию занятия или по фамилии педагога?


class StudioDescription(models.Model):
    """Описание студии"""
    about = models.TextField(verbose_name='О нас', blank=True, null=True)
    philosophy = models.TextField(verbose_name='Философия центра', blank=True, null=True)
    mission = models.TextField(verbose_name='Наша миссия', blank=True, null=True)
    sight = models.TextField(verbose_name='Наш взгляд', blank=True, null=True)
    target = models.TextField(verbose_name='Наша цель', blank=True, null=True)
    logotype = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Логотип', blank=True, null=True)

    class Meta:
        verbose_name = 'О Нас'
        verbose_name_plural = 'О Нас'


###
class Reviews(models.Model):
    """Отзывы о преподавателях и студии"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='Занятие')
    staff = models.ManyToManyField(Staff, verbose_name='Сотрудник')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    message = models.TextField(verbose_name='Текст отзыва')

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
    location = models.CharField(max_length=150, verbose_name='Расположение на карте', blank=True, null=True)
    requisites = models.CharField(max_length=255, verbose_name='Реквизиты', blank=True, null=True)
    starting_work_weekdays = models.TimeField(verbose_name='Начало работы в будние', blank=True, null=True)
    finishing_work_weekdays = models.TimeField(verbose_name='Конец работы в будние', blank=True, null=True)
    starting_work_weekends = models.TimeField(verbose_name='Начало работы по выходным', blank=True, null=True)
    finishing_work_weekends = models.TimeField(verbose_name='Конец работы по выходным', blank=True, null=True)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building}'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
        ordering = ['city']


class SocialNetworks(models.Model):
    """Ссылки на социальные сети"""
    name = models.CharField(max_length=100, verbose_name='Название')
    link = models.CharField(max_length=254, verbose_name='Ссылка')

    # link_1 = models.SlugField(max_length=254, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
        ordering = ['name']


class NewsFlow(models.Model):
    """ Новости портала """
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    digest = models.CharField(max_length=200, verbose_name='Краткое содержание', blank=True, null=True)
    content = models.TextField(verbose_name='Контент')
    media_url = models.URLField(default='', verbose_name='Медиассылка', blank=True,
                                null=True)  # вот тут надо подумать нужно ли
    media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Медиа', null=True, blank=True)
    topic = models.ForeignKey(LessonsType, on_delete=models.CASCADE, verbose_name='Тематика', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified', 'title']  # сортировка
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

class Rent(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    about = models.TextField(verbose_name='Описание аренды')
    media = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name='Медиа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'

class Timetable(models.Model):
    pass #Скорее всего не понадобится отдельная модель, все можно из Lessons вытащить