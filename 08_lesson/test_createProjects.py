from CreateproPage import CreatePro
import os
from dotenv import load_dotenv

load_dotenv()

api = CreatePro("https://ru.yougile.com/api-v2")


def test_create_project():
    token_key = api.get_token()
    print(token_key)

    user_id = os.getenv("USER_ID")
    users = {user_id: "admin"}

    name = "Новый проект 3.1"
    result = api.create_project(name, users)
    print(result)


def test_create_project_negative_invalid_user():
    token_key = api.get_token()
    assert token_key is not None

    invalid_user_id = "00000000-0000-0000-0000-000000000000"
    users = {invalid_user_id: "admin"}

    name = "Проект с невалидным пользователем"
    result = api.create_project(name, users)
    print(result)

    assert (result.get('statusCode')
            in [400, 401, 403, 404]), \
        f"Ожидалась ошибка доступа, получен успех: {result}"

    message = result.get('message', '').lower()
    assert ('user' in message or 'not found' in message
            or 'forbidden' in message)
