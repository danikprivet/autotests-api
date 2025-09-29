import json

json_data = '{"name": "Иван", "age": 30, "is_student": true}'
parsed_data = json.loads(json_data)

print(parsed_data['name'])

data = {
    'name': 'Иван',
    'age': 30,
    'is_student': True,
}

json_string = json.dumps(data)

print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)