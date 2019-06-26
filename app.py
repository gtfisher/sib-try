import json

with open('email-data-live.json') as json_file:
    data = json.load(json_file)
    print(data)
