from ChangePage import ChangePro
import os
from dotenv import load_dotenv

load_dotenv()

api = ChangePro("https://ru.yougile.com/api-v2")
project_id = os.getenv("PROJECTID")


def test_change_project():
    token_key = api.get_token()
    print(token_key)

    title = "Новый проект 5"
    result = api.change_project(project_id, title)
    print(result)


def test_change_project_empty_title():
    token_key = api.get_token()
    assert token_key is not None

    project_id = os.getenv("PROJECTID")
    assert project_id is not None, "Переменная PROJECTID не задана"

    empty_title = ""

    result = api.change_project(project_id, empty_title)
    print(result)

    status_code = result.get('statusCode')
    assert status_code in [400, 422], \
        (f"Ожидалась ошибка валидации для пустого title, "
         f"получен статус: {status_code}")

    message = str(result.get('message', '')).lower()
    assert ('title' in message or 'name' in message
            or 'empty' in message or 'required' in message)
