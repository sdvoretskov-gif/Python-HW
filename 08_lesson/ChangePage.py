import requests
import os
from dotenv import load_dotenv
load_dotenv()


class ChangePro:
    def __init__(self, url) -> None:
        self.url = url

    def get_token(self):
        company_id = str(os.getenv("COMPANYID"))
        creds = {
            "login": os.getenv("LOGIN"),
            "password": os.getenv("PASSWORD"),
            "companyId": company_id}
        resp = requests.post(self.url + "/auth/keys", json=creds)
        return resp.json()

    def change_project(self, project_id, title):
        headers = {'Authorization': f'Bearer {os.getenv("API_TOKEN")}'}
        creds = {
            "title": title
        }
        resp = requests.put(
            self.url + '/projects/' + str(project_id),
            headers=headers, json=creds)
        return resp.json()
