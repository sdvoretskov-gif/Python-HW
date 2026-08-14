from ReceivePage import ReceivePro
import os
from dotenv import load_dotenv

load_dotenv()

api = ReceivePro("https://ru.yougile.com/api-v2")
project_id = os.getenv("PROJECTID")


def test_receive_project():
    token_key = api.get_token()
    print(token_key)
    result = api.receive_project(project_id)
    print(result)


def test_receive_project_negative_invalid_id():
    token_key = api.get_token()
    assert token_key is not None

    invalid_uuid = "00000000-0000-0000-0000-000000000000"

    result = api.receive_project(invalid_uuid)
    print(result)

    status_code = result.get('statusCode')
    assert (status_code ==
            404), (f"Ожидался статус 404 для несуществующего проекта, "
                   f"получен: {status_code}")

    error_msg = result.get('message', '').lower()
    assert 'not found' in error_msg or 'cannot' in error_msg
