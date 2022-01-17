import json

json1 = '{"Name":"Harry", "Age":26, "Department":"HR"}'

python_obj = json.loads(json1)

print(python_obj)

print(python_obj["Name"])