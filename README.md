# My data science projects
From the [Skillfactory Data Science course](http://skillfactory.ru/data-scientist)

## Проекты

[Проект 0. Игра: Угадай число](https://github.com/VicS-Hub2023/DS_Solution/blob/main/game_v3.py)

## Оглавление  
[1. Описание проекта](https://github.com/VicS-Hub2023/DS_Solution/blob/main/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/VicS-Hub2023/DS_Solution/blob/main/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/VicS-Hub2023/DS_Solution/blob/main/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/VicS-Hub2023/DS_Solution/blob/main/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/VicS-Hub2023/DS_Solution/blob/main/README.md#Результат)    
[6. Выводы](https://github.com/VicS-Hub2023/DS_Solution/blob/main/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 10000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Список случайных целых чисел от 1 до 100, длина списка 1000. Каждое число из списка подается по порядку в качестве параметра в функцию «угадыватель».
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
- Инициировать репозиторий
- Клонировать репозиторий на локальную машину
- Скачать архив с базовым решением
- Написать и протестировать бинарный поиск для угадывания числа

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
Реализован бинарный поиск (функция random_predict_binary), который позволяет в среднем угадывать число в интервале от 1 до 100 за 8 попыток.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Бинарный поиск является одним из самых оптимальных алгоритмов для поиска по случайным данным. При поиске случайного значения в интервале от 1 до 100 бинарный поиск в среднем затрачивает стабильно 5 попыток, что сильно превосходит как по качеству, так и по стабильности (стабильность по количеству итераций для нахождения загаданного числа) рандомное угадывание.

:arrow_up:[к оглавлению](.README.md#Оглавление)






