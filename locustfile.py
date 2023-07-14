from locust import HttpUser, task
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Disable self signed certificate warning. 
urllib3.disable_warnings(InsecureRequestWarning)

class BceUser(HttpUser):
    @task
    def awsapp(self):
        # describe page and add header, add auth token in this case
        response = self.client.get("/brf-mgmt", headers={"Cookie": ""})
        #print("Response content: {}".format(response.headers['Server']))

    def on_start(self):
        # Disable to veryfy SSL certification 
        self.client.verify = False
