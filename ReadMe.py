# Работа с Git
# Основная ветка проекта - main
# Рабочая ветка - develop
# Ветки разработчиков - dev_<имя разработчика>, например dev_nikkav79
# Коммиты разработчиков должны быть максимально подробными для того, что бы другие разработчики могли оценить характер
# изменений
# Из веток разработчиков dev_<имя разработчика> данные переносятся в develop.
# после проверки кода в develop информация переносится в main

#Последовательность работы с Git
#1. git checkout develop
#Перед началом работы переключаемся на ветку develop для получения последних данных с удаленного репозитория
#2. git pull 
#Заливаем последние изменения с удаленного репозитория develop
#3. git checkout dev_<твоя ветка>
#Переключаемся на твою ветку
#4. git rebase dev_<твоя ветка> develop
#Получаем последние данные с локальной обновленной develop в твою ветку
#5. работаем с последними данными и вносим изменения в своей ветке
#6. git push -u origin
#Заливаем свою ветку на git в запросом пул реквест


# 14.06.2021 -20.06.2021
# 1. Разработка  models.py
# Таньчик:
# ContactDetails
# SocialNetworks#
#
# Николай:
# StudioDescription
# Status
# Vacancy
# AgeGroups
# AgeLessons (Не уверен что она нужна)
# Lessons
# Media
# Reviews
# Flow (News)
#
# Миша:
# Specialization
# LessonType
# Staff
# Costs
#
#
# 20.06.21-23.06.21
# 2. Заполнение данных БД
# Таньчик:
# ContactDetails
# SocialNetworks#
#
# Николай:
# StudioDescription
# Status
# Vacancy
# AgeGroups
# AgeLessons (Не уверен что она нужна)
# Lessons
# Media
# Reviews
# Flow (News)
#
# Миша:
# Specialization
# LessonType
# Staff
# Costs



