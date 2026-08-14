import requests
import os
from dotenv import load_dotenv
load_dotenv()


class CreatePro:
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

    def create_project(self, name, users):
        headers = {'Authorization': f'Bearer {os.getenv("API_TOKEN")}'}
        company = {"title": name, "users": users}
        resp = (requests.post
                (self.url + '/projects/', headers=headers, json=company))
        return resp.json()
