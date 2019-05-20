# Program symulujący działania czujnika wilgotności:
print("Program symulujący czujnik wilgotności!")

# Wektor temperatur:
humidities = [76.5, 79.4, 80.6, 81.0, 82.8, 83.7, 86.7, 60.8, 68.9, 70.1]
iter = 0

# Importuj bibliotekę Redis do obsługi bazy danych:
import redis

# Połącz się z bazą Redis:
r = redis.Redis()

# Twórz obiekt PubSub:
p = r.pubsub()

# Zasubskrybuj kanał "devices":
p.subscribe("devices")

# Oczekuj, aż coś przyjdzie:
for mes in p.listen():
    print("Odebrano wiadomość:")
    print(mes)
    print(humidities[iter])
    print(r.xadd("d_humi", {"humidity": humidities[iter]}))
    iter = (iter + 1) % len(humidities)
