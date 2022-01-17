import requests
import json

url_name = 'http://httpbin.org/post'
data = {"Name" : "John"}
data_json = json.dumps(data)
h = {'Content-type': 'application/json'}

req_object = requests.post(url_name, data=data_json, headers=h)
print(req_object)