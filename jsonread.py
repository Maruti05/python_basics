import json

with open('E:\Python\PythonBasic\data.json') as json_file:
    data = json.load(json_file)
    print(data)