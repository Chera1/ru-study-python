from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422
    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200
    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200
    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users: dict = {}

        @app.post('/user')
        def post():
            data = request.get_json()
            if not data:
                return {"errors": "User required"}, 400
            elif 'name' in data:
                users[data['name']] = data
                return {"data": f"User {data['name']} is created!"}, 201

        @app.get('/user/<username>')
        def get(username):
            user = users.get(username, None)
            if user:
                return {"data": f"My name is {user['name']}"}, 200
            else:
                return {"data": "User not found"}, 404

        @app.patch('/user/<username>')
        def update(username):
            data = request.get_json()
            if not data:
                return {"errors": "User required"}, 400
            user = users.get(username, None)
            if user:
                users[username].update(data)
                return {"data": f"My name is {data['name']}"}, 200
            else:
                return {"data": "User not found"}, 404

        @app.delete('/user/<username>')
        def delete(username):
            user = users.get(username, None)
            if user:
                users.pop(username)
                return "", 204
            else:
                return {"data": "User not found"}, 404
