# Piklowanie = serializacja
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user: User = User(
    name="John",
    age=15
)


# serializacja
with open('data.pickle', 'wb') as file:
    pickle.dump(user, file)

# deserializacja
with open('data.pickle', 'rb') as file:
    data = pickle.load(file)

print(data.name)
print(data.age)

data_pickle = pickle.dumps(data)
print(data_pickle)

user = pickle.loads(data_pickle)
print(user)
