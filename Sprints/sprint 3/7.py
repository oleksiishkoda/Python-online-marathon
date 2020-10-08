import requests
import json
def get_requests(url):
    return lambda **kwargs: (requests.get(url, params = kwargs)).json()

print("hellooooo")
print("how are u?")