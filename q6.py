#import json

data =[
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]



names = []
for material in data:
    names.append(material['name'])

print(names)



