import json


person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": (
        "engineer",
        "programmer"
    )
}

# Praca na napisach
# encoding
person_json = json.dumps(person, indent=4)
print(person_json)

# decoding
person = json.loads(person_json)
print(person)

# Praca na plikach
with open('data.json', 'w') as file:
    json.dump(person, file)

with open('data.json', 'r')  as file:
    person = json.load(file)

print(person)
