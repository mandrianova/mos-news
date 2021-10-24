## Задача #10: Рекомендательная система новостей для пользователей mos.ru и приложения “Моя Москва”
---
### Описание задачи
Основная задача - изучить сценарии потребления новостей на mos.ru и
разработать рекомендательную систему, предлагающую новости для авторизованных и
неавторизованных пользователей. В решении также нужно предусмотреть
автоматическую разметку новостей по органам исполнительной власти и их
руководителям, тематикам, тегам и др. 

### Требования

###### Ограничения по работе модели:
1. Скорость работы модели < 1 сек.
2. Переобучение модели - не реже 1 раза в день, сокращение времени будет рассматриваться, как дополнительное преимущество.

###### Формат передачи данных:

На вход модели подаются
1. "id" пользователя;

Модель возвращает json со следующими полями:
**"recommendations"** - список рекомендаций следующего формата:
1. "id" - новости;
2. "title" - заголовок новости;
3. "date" - дата публикации новости.

**"history"** - история заказов пользователя, взятая из dataset'а (нужно для быстрого
визуального сравнения):
1. "id" - новости;
2. "title" - заголовок новости;
3. "date" - дата публикации новости.

Результаты должны быть направлены документом в соответствии с шаблоном
result_task3.csv для проверки результатов модели

######Требования к коду:
1. Исходный код должен соответствовать сопроводительной документации;
2. Должна быть обеспечена возможность выполнения процедур сборки и запуска
приведённого кода;
3. Сложные алгоритмические моменты в коде желательно сопроводить
комментариями (будет расцениваться как д ополнительное преимущество).

### Стек:
##### Web:
- [FastAPI](https://github.com/tiangolo/fastapi "современный, шустрый веб-фреймворк для строительства API c помощью Python => 3.6")
- [pydantic](https://github.com/samuelcolvin/pydantic "валидация данных и настройки с применением встроенных аннотаций типов Python")
- Uvicorn (https://github.com/encode/uvicorn)
##### Auto-markup:
- nltk (https://github.com/nltk/nltk)
- pymorphy2 (https://github.com/kmike/pymorphy2/blob/92d546f042ff14601376d3646242908d5ab786c1/docs/index.rst)
- natasha (https://github.com/natasha/natasha)
##### Recommendations:
- implicit, модель ItemItemRecommender 
(https://github.com/benfred/implicit/blob/main/docs/quickstart.rst,
 https://github.com/benfred/implicit/blob/main/implicit/nearest_neighbours.py#L12)

### Деплой и нюансы
#### Руководство по запуску

1. Шаг первый - установить все пакеты:
    ```pip install -r requirements.txt```
2. Шаг второй - поднять сервер:
    ```uvicorn main:app --reload```
3. Proceed to http://127.0.0.1:8000/
4. Run task update model and choose "auto_markup" to generate required files. This task needs some time (~10 min). So, relax and don't hurry!
5. Now push get / post
6. Repeat
7. Good evening

#### Запуск с docker-compose

- Команда для jupyter:
```docker-compose up jupyter``` 
Use host and port http://127.0.0.1:8089/
- Команда для web-service:
```docker-compose up web```
Use host and port http://127.0.0.1:8090/
