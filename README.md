## Задача #10: Рекомендательная система новостей для пользователей mos.ru и приложения “Моя Москва”
---

### Описание задачи
Основная задача - изучить сценарии потребления новостей на mos.ru и разработать рекомендательную систему, предлагающую новости для авторизованных и неавторизованных пользователей. В решении также нужно предусмотреть автоматическую разметку новостей по органам исполнительной власти и их руководителям, тематикам, тегам и др. 

### Решение

[Демонстрационный стенд](http://217.28.231.202/docs#/)
[Интерфейс рекомендаций](http://217.28.231.202:8080/)

[Сопроводительная документация](/develop/Documentation.ipynb)

- [result_task10.csv](/develop/result_task10.csv) для проверки результатов модели
- [метод для получения рекомендаций http://217.28.231.202/recommendations/id](http://217.28.231.202/recommendations/1)

Дополнительные методы:

http://217.28.231.202/docs

- /auto_markup/generate_markups - метод post для получения списка тегов и сфер для новости (принимает title, preview, full_text)
- /update_model - метод get для запуска обновления данных для моделей. Принимает model_name, возвращает id задачи для отслеживания статуса обновления
- /status/task_id - метод get для получения статуса задачи. Принимает id задачи, возвращает статус выполнения.


### Структура кода
- main.py - базовый скрипт для запуска fastapi
- save_history - скрипт для формирования истории просмотров в заданном формате
- recommendations - подсистема рекомендаций (cold_rec - формирование рекомендаций для новых пользователей, rec - для формирования рекомендаций на основе датасета, managers - обработчики)
- auto_markup - подсистема для формирования авторазметки (support_for_model - логика для алгоритма авторазметки, model.py - функции для обработки документа)
- data - файлы с данными
- develop - черновые notebooks-файлы и результирующий csv.

### Применяемый стек:
##### Веб-сервер и API:
- [FastAPI](https://github.com/tiangolo/fastapi "современный, шустрый веб-фреймворк для строительства крутых API c помощью Python => 3.6")
- [Pydantic](https://github.com/samuelcolvin/pydantic "валидация данных и настройки с применением встроенных аннотаций типов Python")
- [Uvicorn](https://github.com/encode/uvicorn "лёгкий и стремительный ASGI-сервер")
- [Vue.js](https://vuejs.org/ "прогрессивный JavaScript FrameWork")
- [Vuetify](https://vuetifyjs.com/ "Material Design Front-End FrameWork")

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

3. Для доступа к API и Swagger-документации откройте браузер и проследуйте по адрусу http://127.0.0.1:8000/
4. Для запуска локального фронтенд сервера в режиме разработки перейдите в директорию frontend и запустите в терминале на выбор:

    ```npm run serve или yarn serve```

    далее проследуйте по адрусу http://127.0.0.1:8080/

##### Вариант запуска с помощью [docker](https://www.docker.com "популярный контейнизатор")

- Установка всех зависимостей и запуск локального сервера:

```docker-compose up web```

с целью минимизации каких-либо конфликтов доступ реализован через альтернативный порт http://127.0.0.1:8090/
собственно, на этом всё. за это и любят docker)

- Запуск локального frontend-сервера :
  
  ```docker-compose up frontend```

на всякий случай, добавили ноутбук для быстрых проверок

- Запуск jupyter notebook:
  
```docker-compose up jupyter```

аналогичная ситуация - обратите внимание на альтернативный порт http://127.0.0.1:8089/
