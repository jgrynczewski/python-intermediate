# Pythonowe funkcje do pracy z wyrażeniami regularnymi
from typing import Match, Pattern, Iterator
import re

print(dir(re))

text: str = """The car was moving across the street.
Maybe, the traffic was heavy ?!"""

pattern: str = r"the"

# search: znajduje pierwsze dopasowanie (obiekt klasy Match)
result: Match = re.search(pattern, text)
print(result)

print(result.group())
print(result.start())
print(result.end())


# finditer: pozwala przeiterować się po wszystkich dopasowaniach (obiektach klasy iter)
result2: Iterator = re.finditer(pattern, text)
print(result2)

for item in result2:
    print(item)

# match: dopasowuje cały napis (odpowiednik funkcji search z patternem uzupełnionym o znak ^ na początku i znak $ na końcu)
result2: Match = re.match(pattern, text)
print(result2)

# findall: znajduje wszystkie dopasowania i zwraca listę dopasowanych napisów
result4: list = re.findall(pattern, text)
print(result4)

# Grupy nazwane w pythonie
number = "123-456-789"
pattern: str = r"^(?P<first>\d{3})[- ]?(?P<second>\d{3})[- ]?(?P<third>\d{3})$"
result5: Match = re.search(pattern, number)
print(result5.group(1))
print(result5.group('first'))
print(result5.groups())

blocked_words = r"the|was"

# sub: podstawia w miejsce dopasowania napis podany w drugim argumencie
result6: str = re.sub(blocked_words, "...", text)
print(result6)

pattern = r"\s"

# split: rozbija tekst, gdzie separatorem są wszystkie dopasowania
result7: list = re.split(pattern, text)
print(result7)

# Podejście alternatywne
# compile: pozwala na przygotowanie obiektu, który będzie wykorzystywany do wyszukiwania wzorca
# przydatne kiedy wiemy, że będziemy przeszukiwali wiele dokumentów. Możemy w ten sposób trochę zaoszczędzić tworząc
# ten obiekt raz, a nie przy nowym dokumencie.
pattern: Pattern = re.compile(r"the")
result8: Match = pattern.search(text)
print(result8)