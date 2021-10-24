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

##### Требования к коду:
1. Исходный код должен соответствовать сопроводительной документации;
2. Должна быть обеспечена возможность выполнения процедур сборки и запуска
приведённого кода;
3. Сложные алгоритмические моменты в коде желательно сопроводить
комментариями (будет расцениваться как д ополнительное преимущество).

### Применяемый стек:
##### Веб-сервер и API:
- [FastAPI](https://github.com/tiangolo/fastapi "современный, шустрый веб-фреймворк для строительства крутых API c помощью Python => 3.6")
- [Pydantic](https://github.com/samuelcolvin/pydantic "валидация данных и настройки с применением встроенных аннотаций типов Python")
- [Uvicorn](https://github.com/encode/uvicorn "лёгкий и стремительный ASGI-сервер")
##### Авторазметка:
- [nltk](https://github.com/nltk/nltk "набор инструментов для обработки текста NLTK -- the Natural Language Toolkit")
- [pymorphy2](https://github.com/kmike/pymorphy2/blob/92d546f042ff14601376d3646242908d5ab786c1/docs/index.rst "Морфологический анализатор pymorphy2 -> приводит слова к нормальной форме, а также многое другое")
- [natasha](https://github.com/natasha/natasha "библиотека для обработки текстов на русском языке")
##### Рекомендации:
- [implicit](https://github.com/benfred/implicit/blob/main/docs/quickstart.rst)
- [модель ItemItemRecommender](https://github.com/benfred/implicit/blob/main/implicit/nearest_neighbours.py#L12)

### Деплой и прочие нюансы
#### Руководство по запуску

##### Вариант с созданием виртуального окружения
1. Шаг первый - после создания и активации виртуального окружения установите все необходимые зависимости с помощью:
    ```pip install -r requirements.txt```

    если возникли вопросы, то загляните на [этот сайт](https://realpython.com/python-virtual-environments-a-primer/)
2. Шаг второй - запустите сервер сервер:
    ```uvicorn main:app --reload```

    убедитесь, что у вас активировано виртуальное окружение.
3. Откройте браузер и проследуйте http://127.0.0.1:8000/

##### Вариант запуска с помощью [docker](https://www.docker.com "популярный контейнизатор")

- Установка всех зависимостей и запуск локального сервера:

```docker-compose up web```

с целью минимизации каких-либо конфликтов доступ реализован через альтернативный порт http://127.0.0.1:8090/
собственно, на этом всё. за это и любят docker)

на всякий случай, добавили ноутбук для быстрых проверок
- Запуск jupyter notebook:
  
```docker-compose up jupyter```

аналогичная ситуация - обратите внимание на альтернативный порт http://127.0.0.1:8089/
