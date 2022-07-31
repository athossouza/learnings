import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/get/json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp.status_code)
print(resp)
