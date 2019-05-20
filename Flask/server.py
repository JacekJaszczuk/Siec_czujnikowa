# Importuj bibliotekę Redis do obsługi bazy danych:
import redis

# Połącz się z bazą Redis:
r = redis.Redis()

# Importuj Flask:
from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route("/")
def hello():
    # Pobierz dane z bazy:
    data = r.xrange("d_temp", count=10)
    print(data)

    # Zapisz temperatury:
    temperatury = []
    for val in data:
        temperatury.append(float(val[1][b"temperature"]))
    print(temperatury)

    return render_template("hello.html", temp=str(temperatury))
