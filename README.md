## API для блога-платформы YaTube
Реализация API сервиса публикации личных дневников YaTube

## Функциональные возможности:

* Позволяет получить список всех публикаций;
* Создать новую публикацию, при условии, что пользователь авторизован;
* Обновить, получить и удалить публикацию по ID
* Получить все комментарии к публикации по ID;
* Создать комментарий;
* Вывести комментарий по ID;
* Обновить, удалить комментарий по ID;
* Используется JWT-токен;
* Возможность получить всех подписчиков/создать подписку;
* Возможность получить список всех групп/создать новую группу;

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Igry44ik/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры

* ### Получение токена авторизации
    **Request**
    ```
        POST /api/v1/token/
        body: {"username": "string", "password": "string"}
    ```
    **Response**
    ```
        {
          "refresh": "<JRW-refresh-token>",
          "access": "<JRW-access-token>",
        }
    ```

* ### Обновление токена
    **Request**
    ```
        POST /api/v1/token/refresh/
        body: {"refresh": "JRW-refresh-token"}
    ```
    **Response**
    ```
        {
          "access": "<new-JRW-access-token>"
        }
    ```

* ### Получение списка всех публикаций
    **Request**
    ```
        GET /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    ```

* ### Создание новой публикации
    **Request**
    ```
        POST /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Получение публикации по id
    **Request**
    ```
        GET /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Обновление публикации по id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Частичное обновление публикации по id
    **Request**
    ```
        PATCH /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Удаление публикации по id
    **Request**
    ```
        DELETE /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 204
    ```

* ### Получение списка всех комментариев
    #### Request
    ```
        GET /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    ```

* ### Создание нового комментария
    **Request**
    ```
        POST /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Получение комментария по id
    **Request**
    ```
        POST /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Обновление комментария по id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Частичное обновление комментария по id
    **Request**
    ```
        PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ### Удаление комментария по id
    #### Request
    ```
        DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 204
    ```

* ### Получение списка всех подписчиков
    **Request**
    ```
        GET /api/v1/follow/?search={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "user": "string",
                "following": "string"
            },
            ...
        ]
    ```

* ### Создание подписки
    **Request**
    ```
        POST /api/v1/follow/?user={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"following": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "user": "string",
            "following": "string"
        }
    ```

* ### Получение списка всех групп
    **Request**
    ```
        GET /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "title": "string"
            },
            ...
        ]
    ```

* ### Создание новой группы
    **Request**
    ```
        POST /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"title": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "title": "string"
        }
    ```
