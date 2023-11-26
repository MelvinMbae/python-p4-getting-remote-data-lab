import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        request=requests.get(self.url)
        return request.content

    def load_json(self):
        json_body=json.loads(self.get_response_body())
        return json_body