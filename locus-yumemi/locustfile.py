import time 
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    def __init__(self, parent):
        super().__init__(parent)
        self.token = ""

    wait_time = between(1, 2)

    def on_start(self): 
        with self.client.get(url="/login") as response:
            # self.token = response.json()["token"]
            self.client.headers = {'Authorization': response.json()["token"]}

    @task
    def index_page(self):
        self.client.get(url="/hello")

    @task
    def slow_page(self):
        self.client.get(url="/slow")

    @task
    def secret_page(self):
        self.client.get(url="/secret")
