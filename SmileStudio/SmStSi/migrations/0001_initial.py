# Generated by Django 3.2.4 on 2021-06-20 19:04

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание ')),
            ],
            options={
                'verbose_name': 'Возрастная группа',
                'verbose_name_plural': 'Возрастные группы',
            },
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('district', models.CharField(max_length=150, verbose_name='Район')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('building', models.CharField(max_length=10, verbose_name='Дом')),
                ('postcode', models.PositiveBigIntegerField(verbose_name='Индекс')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта')),
                ('location', models.CharField(blank=True, max_length=150, verbose_name='Расположение на карте')),
            ],
            options={
                'verbose_name': 'Контактные данные',
                'verbose_name_plural': 'Контактные данные',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Стоимость',
                'verbose_name_plural': 'Стоимости',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50, verbose_name='Длительность')),
                ('days', models.CharField(max_length=100, verbose_name='Дни')),
                ('hours', models.CharField(max_length=100, verbose_name='Часы')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актив')),
                ('cost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.costs')),
                ('lesson_age', models.ManyToManyField(to='SmStSi.AgeGroups')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
            },
        ),
        migrations.CreateModel(
            name='LessonsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип урока',
                'verbose_name_plural': 'Типы уроков',
            },
        ),
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Название')),
                ('link', models.CharField(blank=True, max_length=254, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актив')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип договора')),
            ],
            options={
                'verbose_name': 'Тип договора',
                'verbose_name_plural': 'Типы договора',
            },
        ),
        migrations.CreateModel(
            name='StudioDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='О нас')),
                ('philosophy', models.TextField(verbose_name='Философия центра')),
                ('mission', models.TextField(verbose_name='Наша миссия')),
                ('sight', models.TextField(verbose_name='Наш взгляд')),
                ('target', models.TextField(verbose_name='Наша цель')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('responsibilities', models.TextField(verbose_name='Обязанности')),
                ('requirements', models.TextField(verbose_name='Требования')),
                ('conditions', models.TextField(verbose_name='Условия')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актив')),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.specialization')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.status')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['date_add'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('experience', models.CharField(max_length=150, verbose_name='Опыт')),
                ('education', models.CharField(max_length=150, verbose_name='Образование')),
                ('ad_information', models.TextField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Актив')),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.specialization')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.status')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('message', models.TextField()),
                ('star_choice_1', models.CharField(max_length=5, verbose_name='Рейтинг1')),
                ('star_choice_2', models.CharField(max_length=5, verbose_name='Рейтинг2')),
                ('star_choice_3', models.CharField(max_length=5, verbose_name='Рейтинг3')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.lessons')),
                ('staff_id', models.ManyToManyField(to='SmStSi.Staff')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.users')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('photo_link', models.ImageField(upload_to='post_files')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='post_files')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.lessons')),
                ('staff_id', models.ManyToManyField(to='SmStSi.Staff')),
            ],
            options={
                'verbose_name': 'Медиа',
                'verbose_name_plural': 'Медиа',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='lessons',
            name='lesson_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.lessonstype'),
        ),
        migrations.AddField(
            model_name='costs',
            name='lesson_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.lessonstype'),
        ),
        migrations.AddField(
            model_name='costs',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmStSi.staff'),
        ),
    ]
