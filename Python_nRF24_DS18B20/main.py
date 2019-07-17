import requests
import json
from dongiel import Dongiel
import datetime

print("Program czytający temperaturę z seriala i wysyłający ją do API")

# Twórz obiekt do obsługi dongla nRF24:
dongiel = Dongiel()

# Adres API:
#api_url = "http://192.168.0.20:8000/aplikacja/api"
api_url = "http://rejapi.ml:8000/aplikacja/api"

# Słownik z danymi:
slownik = {"data": datetime.datetime.now().date().isoformat(), "miejsce": 6, "pacjent": 4, "typ_pomiaru": "Temperatura", "wartosc": 27.6}

while True:
    # Odczytaj temperaturę z seriala:
    json_temp = dongiel.recv()

    # Wyrzuć niepotrzebne zera i znak nowej linii:
    json_temp = json_temp[0:json_temp.find(b"\n")]
    print("Udało się coś odczytać z seriala! {}".format(json_temp))

    # Odczytaj temperaturę:
    temp = json.loads(json_temp)["temperature"]

    # Przygotuj słownik:
    slownik["data"] = datetime.datetime.now().date().isoformat()
    slownik["wartosc"] = temp

    # Zamień słownik na JSONa:
    json_str = json.dumps(slownik)

    # Wyślij dane do API
    r = requests.post(api_url, json_str)
    if r.status_code == 200:
        print("Udało się wysłać do API!")
    else:
        print("Coś poszło nie tak z API.")