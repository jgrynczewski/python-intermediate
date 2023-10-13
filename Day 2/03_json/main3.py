# Klasowe encodery i dekodery json
from typing import Any
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


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, User):
            return {
                'name': o.name,
                'age': o.age,
                o.__class__.__name__: True
            }
        else:
            super().default(o)


data_json = json.dumps(data, cls=MyJSONEncoder)
print(data_json)


class MyJSONDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, dct):
        if User.__name__ in dct:
            return User(
                name=dct.get('name'),
                age=dct.get('age')
            )
        else:
            return dct


data = json.loads(data_json, cls=MyJSONDecoder)
print(data)
