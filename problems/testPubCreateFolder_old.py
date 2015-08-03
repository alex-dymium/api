import requests
import json

method = 'POST'
url = '<domein/endpoint/path>'
headers = dict()
headers['Content-Type'] = 'application/json'
data = dict()
data['action'] = 'add_folder'
username = 'username'
password = 'pass'

data = json.dumps(data)

r = requests.request(
    method=method,
    url=url,
    headers=headers,
    data=data,
    auth=(username, password)
)

try:
    json_resp = json.loads(r.content)
except ValueError:
    json_resp = 'NoJSON'

print(json_resp)
print()
print(r.status_code)
print()
print(r.headers)
