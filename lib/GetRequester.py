import requests
import json

class GetRequester:

    def __init__(self, url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        json_data = json.loads(response_body)
        return json_data

# Example usage:
requester_instance = GetRequester()

# Get the response body
response_body = requester_instance.get_response_body()
print("Response Body:")
print(response_body)

# Load JSON data
json_data = requester_instance.load_json()
print("\nJSON Data:")
print(json_data)
