import json

sampleJson = {"id" : 2, "name": "values", "age" : 29}

a_json = json.dumps(sampleJson, sort_keys=True)

print(a_json)

with open('data.json', 'w') as f:
    json.dump(sampleJson, f, indent=4)