# Program do "szturchania" urządzeń w celu przesłania wyników co minutę:
print("Program szturchacz!")

# Importuj bibliotekę Redis do obsługi bazy danych:
import redis

# Inne biblioteki:
import time

# Połącz się z bazą Redis:
r = redis.Redis()

while True:
    print("Szturchaniec")
    r.publish("devices", "szturchaniec")
    time.sleep(60)