import tomllib


with open('example.toml', 'rb') as file:
    data = tomllib.load(file)

print(data)
