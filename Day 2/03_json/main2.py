# Funkcyjne encodery i decodery json
# Python nie wie jak przedstawić nasze klasy w jsonie (encoding), ani jak z jsona otrzymać nasze klasy (decoding).
# Musimy mu to powiedzieć.
import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)

data = {
    "type": "person",
    "user": user
}


# json_data = json.dumps(data)  # TypeError  - python nie umie
def my_encode(o):
    if isinstance(o, User):
        return {
            'name': o.name,
            'age': o.age,
            o.__class__.__name__: True
        }
    else:
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")


json_data = json.dumps(data, default=my_encode)
print(json_data)


def my_decode(dct):
    if User.__name__ in dct:
        return User(
            name=dct.get('name'),
            age=dct.get('age')
        )
    else:
        return dct


data = json.loads(json_data, object_hook=my_decode)
print(data)
