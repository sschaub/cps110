import json

fireFile = open('fires.json')

fileData = fireFile.read()
records = json.loads(fileData)

for rec in records:
    print(rec['street'], rec['station'])

    