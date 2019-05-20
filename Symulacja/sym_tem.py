# Program symulujący działania czujnika temperatury:
print("Program symulujący czujnik temperatury!")

# Wektor temperatur:
temperatures = [22.3, 21.7, 20.5, 18.9, 18.6, 17.5, 18.7, 19.9, 23.1, 23.4]
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
    print(temperatures[iter])
    print(r.xadd("d_temp", {"temperature": temperatures[iter]}))
    iter = (iter + 1) % len(temperatures)
