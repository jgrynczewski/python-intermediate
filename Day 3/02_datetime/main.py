from datetime import time, date, datetime
print(dir(datetime))  # co moduł datetime potrafi?

# tworzenie
d: date = date(1999, 10, 9)
t: time = time(2, 12, 45)
dt: datetime = datetime(1999, 10, 9, 2, 12, 45)

dt2 = datetime.combine(d, t)

# atrybuty
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

print(dt.date())
print(dt.time())

# Aktualna data/czas
dt_now: datetime = datetime.now()
d_today: date = date.today()


# format ISO 8601  1999-10-09T02:12:45+01:00
print(dt.isoformat())

print(dt.weekday())  # monday - 0
print(dt.isoweekday())  # monday - 1

dt = datetime.fromisoformat("1999-10-09T02:12:45")
print(dt)


# formatting
# konwersja do napisu
dt = datetime.now()

print(datetime.strftime(dt, "%Y"))
print(dt.strftime("%Y"))

print(dt.strftime("%Y-%m-%dT%H:%M:%S"))
print(dt.strftime("%c"))

# konwersja z napisu
x = '1999-02-22 02:34:01'

dt = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
print(dt)

# Działania na obiektach datetime
dt = datetime(2013, 8, 12)
result = datetime.now() - dt  # timedelta
print(result)


# Interwał czasowy - klasa timedelta
from datetime import timedelta

print(datetime.now() + timedelta(minutes=15))
print(datetime.now() - timedelta(weeks=2))
print(datetime.now() - timedelta(days=2, hours=3, minutes=5))

interval = timedelta(
    weeks=2, days=2, hours=5
)

print(datetime.now() > dt)

# timestamp unix
timestamp = datetime.timestamp(dt)
print(timestamp)
print(dt.timestamp())

dt = datetime.fromtimestamp(timestamp)

# Wsparcie dla stref czasowych

from datetime import timezone

now = datetime.now(tz=timezone.utc)
print(now)

# biblioteka ZoneInfo zawiera informacje o strefach czasowych
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
local_tz = ZoneInfo("Europe/Warsaw")

dt = datetime(2013, 8, 12, tzinfo=local_tz)
print(dt)

print(dt.tzname())


# Moduł calendar (praca z kalendarzem)
import calendar

print(dir(calendar))

calendar = calendar.HTMLCalendar()
result = calendar.formatmonth(2023, 9)

with open('cal.html', 'w') as file:
    file.write(result)


# moduł time
import time
time.time()  # unix timestamp

time.sleep(5)  # wstrzymuje wykonywanie głównej pętli programu na wskazaną liczbę sekund
